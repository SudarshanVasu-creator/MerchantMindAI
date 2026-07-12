import csv
from pathlib import Path
from typing import Any

from app.core.logging import logger

BASE_DIR = Path(__file__).resolve().parent.parent.parent
INVENTORY_FILE = BASE_DIR / "sample_data" / "inventory.csv"


def load_inventory() -> list[dict[str, Any]]:
    """
    Load inventory data from the sample dataset.
    """

    logger.info("Loading inventory data...")

    with open(INVENTORY_FILE, "r", encoding="utf-8") as file:
        inventory = list(csv.DictReader(file))

    logger.info("Loaded %d inventory items.", len(inventory))

    return inventory