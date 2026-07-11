from app.core.logging import logger
from app.graph.state import BusinessState


def chief_business_officer(state: BusinessState) -> BusinessState:
    """
    Entry point of MerchantMind AI.
    """

    logger.info("Chief Business Officer started analysis.")

    return state