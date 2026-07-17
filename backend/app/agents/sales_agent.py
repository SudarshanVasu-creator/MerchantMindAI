from app.core.logging import logger
from app.graph.state import BusinessState
from app.services.llm import LLMService
from app.services.metrics import build_sales_intelligence
from app.tools.prompt_loader import load_prompt
from app.tools.sales_loader import load_sales


def sales_agent(state: BusinessState) -> BusinessState:
    """
    Analyze sales data using Gemini.
    """

    logger.info("Sales Agent started.")

    sales = load_sales()

    intelligence = build_sales_intelligence(sales)

    prompt = load_prompt(
        "sales_agent.j2",
        business_name=state["business_name"],
        sales_metrics=intelligence,
    )

    llm = LLMService()

    analysis = llm.invoke_json(prompt)

    state["sales"] = sales
    state["sales_metrics"] = intelligence
    state["sales_analysis"] = analysis
    state.pop("sales", None)

    logger.info("Sales Agent finished.")

    return state