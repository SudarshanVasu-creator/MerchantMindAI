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
        "gemini-3.5-flash"
    )

    GROQ_API_KEY: str = os.getenv(
        "GROQ_API_KEY",
        "",
    )

    GROQ_BASE_URL: str = os.getenv(
        "GROQ_BASE_URL",
        "https://api.groq.com/openai/v1",
    )

    GROQ_MODEL: str = os.getenv(
        "GROQ_MODEL",
        "openai/gpt-oss-120b",
    )

    # Future Provider Support

    OPENROUTER_API_KEY: str = os.getenv("OPENROUTER_API_KEY", "")

    OPENROUTER_BASE_URL: str = os.getenv(
        "OPENROUTER_BASE_URL",
        "https://openrouter.ai/api/v1",
    )


settings = Settings()