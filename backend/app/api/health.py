from fastapi import APIRouter

from app.config import settings
from app.core.logging import logger

router = APIRouter()


@router.get("/", tags=["Health"])
def health_check():
    """Health check endpoint."""

    logger.info("Health endpoint accessed.")

    return {
        "project": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "status": "Running",
    }


