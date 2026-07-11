from fastapi import FastAPI
from app.core.logging import logger
from app.config import settings

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
)

logger.info("MerchantMind AI backend started.")

@app.get("/", tags=["Health"])
def health_check():
    logger.info("Health endpoint accessed.")
    return {
        "project": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "status": "Running",
    }