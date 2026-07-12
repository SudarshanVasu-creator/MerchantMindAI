from pathlib import Path

from dotenv import load_dotenv
import os

# Project Paths
BASE_DIR = Path(__file__).resolve().parent.parent
ENV_FILE = BASE_DIR / ".env"

# Load environment variables
load_dotenv(ENV_FILE)


class Settings:
    """Application configuration."""

    APP_NAME: str = os.getenv("APP_NAME", "MerchantMind AI")
    APP_VERSION: str = os.getenv("APP_VERSION", "0.1.0")
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "development")

    # LLM Configuration

    GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY", "")

    DEFAULT_MODEL: str = os.getenv(
        "DEFAULT_MODEL",
        "gemini-2.5-flash"
    )

    # Future Provider Support

    OPENROUTER_API_KEY: str = os.getenv("OPENROUTER_API_KEY", "")

    OPENROUTER_BASE_URL: str = os.getenv(
        "OPENROUTER_BASE_URL",
        "https://openrouter.ai/api/v1",
    )


settings = Settings()