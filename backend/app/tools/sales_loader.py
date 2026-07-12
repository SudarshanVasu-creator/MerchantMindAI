import csv
from pathlib import Path
from typing import Any

from app.core.logging import logger


BASE_DIR = Path(__file__).resolve().parent.parent.parent
SALES_FILE = BASE_DIR / "sample_data" / "sales.csv"


def load_sales() -> list[dict[str, Any]]:
    """
    Load sales data from the sample dataset.
    """

    logger.info("Loading sales data...")

    with open(SALES_FILE, "r", encoding="utf-8") as file:
        sales = list(csv.DictReader(file))

    logger.info("Loaded %d sales records.", len(sales))

    return sales