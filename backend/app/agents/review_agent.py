from app.core.logging import logger
from app.graph.state import BusinessState
from app.services.llm import LLMService
from app.services.metrics import build_review_intelligence
from app.tools.prompt_loader import load_prompt
from app.tools.review_loader import load_reviews


def review_agent(state: BusinessState) -> BusinessState:
    """
    Loads customer reviews into the workflow state.
    """

    logger.info("Review Agent started.")

    reviews = load_reviews()

    intelligence = build_review_intelligence(reviews)

    prompt = load_prompt(
        "review_agent.j2",
        business_name=state["business_name"],
        review_intelligence=intelligence,
    )

    llm = LLMService()

    analysis = llm.invoke_json(prompt)

    state["review_intelligence"] = intelligence
    state["review_analysis"] = analysis
    state.pop("reviews", None)

    logger.info("Prompt rendered successfully.")
    logger.info("Review Agent finished.")

    return state