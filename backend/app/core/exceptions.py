from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.core.logging import logger


class LLMProviderError(Exception):
    """
    Base exception for all LLM provider errors.
    """


class ProviderUnavailableError(LLMProviderError):
    """
    Temporary provider failure.
    Examples:
    - HTTP 503
    - Timeout
    - Network issue
    """


class ProviderQuotaExceededError(LLMProviderError):
    """
    Provider quota exhausted.
    Example:
    - HTTP 429
    """


class ProviderAuthenticationError(LLMProviderError):
    """
    Invalid API key or authentication failure.
    Example:
    - HTTP 401
    - HTTP 403
    """


class ProviderBadRequestError(LLMProviderError):
    """
    Invalid request sent to provider.
    Example:
    - HTTP 400
    """


def register_exception_handlers(app: FastAPI) -> None:
    """Register global exception handlers."""

    @app.exception_handler(Exception)
    async def global_exception_handler(request: Request, exc: Exception):
        logger.exception(
            f"Unhandled exception on %s %s",
            request.method,
            request.url.path,
        )

        return JSONResponse(
            status_code=500,
            content={
                "error": "Internal Server Error",
                "message": "Something went wrong.",
                "status": 500,
            },
        )