from app.core.logging import logger
from app.graph.state import BusinessState
from app.tools.review_loader import load_reviews


def review_agent(state: BusinessState) -> BusinessState:
    """
    Loads customer reviews into the workflow state.
    """

    logger.info("Review Agent started.")

    reviews = load_reviews()

    state["reviews"] = reviews

    logger.info("Review Agent finished.")

    return state