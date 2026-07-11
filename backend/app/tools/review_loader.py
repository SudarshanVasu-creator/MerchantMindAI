import json
from pathlib import Path
from typing import Any
from app.core.logging import logger


BASE_DIR = Path(__file__).resolve().parent.parent.parent
REVIEWS_FILE = BASE_DIR / "sample_data" / "reviews.json"




def load_reviews() -> list[dict[str, Any]]:
    """
    Load customer reviews from the sample dataset.
    """

    logger.info("Loading customer reviews...")

    with REVIEWS_FILE.open("r", encoding="utf-8") as file:
        reviews = json.load(file)

    logger.info(f"Loaded {len(reviews)} reviews.")

    return reviews