from fastapi import FastAPI

from app.api.health import router as health_router
from app.config import settings
from app.core.exceptions import register_exception_handlers
from app.core.logging import logger

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
)

register_exception_handlers(app)
app.include_router(health_router)
logger.info("MerchantMind AI backend started.")