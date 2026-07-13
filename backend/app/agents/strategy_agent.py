import json

from app.core.logging import logger
from app.graph.state import BusinessState
from app.services.llm import LLMService
from app.tools.prompt_loader import load_prompt


def strategy_agent(state: BusinessState) -> BusinessState:
    """
    Generate a business strategy based on previous analyses.
    """

    logger.info("Strategy Agent started.")

    review_analysis = json.dumps(
        state["review_analysis"],
        indent=2,
        ensure_ascii=False,
    )

    sales_analysis = json.dumps(
        state["sales_analysis"],
        indent=2,
        ensure_ascii=False,
    )

    inventory_analysis = json.dumps(
        state["inventory_analysis"],
        indent=2,
        ensure_ascii=False,
    )

    marketing_plan = json.dumps(
        state["marketing_plan"],
        indent=2,
        ensure_ascii=False,
    )

    prompt = load_prompt(
        "strategy_agent.j2",
        business_name=state["business_name"],
        review_analysis=review_analysis,
        sales_analysis=sales_analysis,
        inventory_analysis=inventory_analysis,
        marketing_plan=marketing_plan,
    )

    llm = LLMService()

    analysis = llm.invoke_json(prompt)

    state["strategy"] = analysis

    logger.info("Strategy Agent finished.")

    return state