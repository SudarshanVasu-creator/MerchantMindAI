import json

from app.core.exceptions import (
    ProviderAuthenticationError,
    ProviderBadRequestError,
    ProviderQuotaExceededError,
    ProviderUnavailableError,
)
from app.core.logging import logger
from app.services.providers.gemini_provider import GeminiProvider
from app.services.providers.groq_provider import GroqProvider


class LLMService:
    """
    Handles communication with available LLM providers.
    Automatically falls back if the primary provider fails.
    """

    def __init__(self):

        self.providers = [
            GeminiProvider(),
            GroqProvider(),
        ]

    def invoke(self, prompt: str) -> str:
        """
        Send a prompt to the first available provider.
        """

        last_exception = None

        for provider in self.providers:

            provider_name = provider.__class__.__name__

            try:

                logger.info(
                    "Trying provider: %s",
                    provider_name,
                )

                response = provider.invoke(prompt)

                logger.info(
                    "Provider succeeded: %s",
                    provider_name,
                )

                return response

            except (
                ProviderQuotaExceededError,
                ProviderUnavailableError,
            ) as e:

                logger.warning(
                    "Provider %s unavailable: %s",
                    provider_name,
                    e,
                )

                last_exception = e

                continue

            except (
                ProviderAuthenticationError,
                ProviderBadRequestError,
            ) as e:

                logger.warning(
                    "Provider %s failed: %s",
                    provider_name,
                    e,
                )

                last_exception = e

                continue

        if last_exception:
            raise last_exception

        raise RuntimeError("No LLM providers are configured.")

    def invoke_json(self, prompt: str) -> dict:
        """
        Send a prompt and parse JSON.
        """

        response = self.invoke(prompt)

        response = (
            response
            .replace("```json", "")
            .replace("```", "")
            .strip()
        )

        try:
            return json.loads(response)

        except json.JSONDecodeError:

            logger.exception(
                "Failed to parse JSON returned by provider."
            )

            raise