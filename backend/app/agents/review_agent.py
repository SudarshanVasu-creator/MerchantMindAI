from app.core.logging import logger
from app.graph.state import BusinessState
from app.services.llm import LLMService
from app.tools.prompt_loader import load_prompt
from app.tools.review_loader import load_reviews



def review_agent(state: BusinessState) -> BusinessState:
    """
    Loads customer reviews into the workflow state.
    """

    logger.info("Review Agent started.")

    reviews = load_reviews()
    
    prompt = load_prompt(
        "review_agent.j2",
        business_name=state["business_name"],
        reviews=reviews,
    )

    llm = LLMService()

    analysis = llm.invoke_json(prompt)
    
    state["reviews"] = reviews
    state["review_analysis"] = analysis

    logger.info("Prompt rendered successfully.")
    logger.info("Review Agent finished.")

    return state