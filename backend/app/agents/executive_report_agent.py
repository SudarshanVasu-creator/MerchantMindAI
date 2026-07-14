import json
from datetime import datetime

from app.core.logging import logger
from app.graph.state import BusinessState
from app.services.llm import LLMService
from app.tools.prompt_loader import load_prompt


def executive_report_agent(state: BusinessState) -> BusinessState:
    """
    Generate the final executive business report.
    """

    logger.info("Executive Report Agent started.")

    generated_date = datetime.now().strftime("%B %d, %Y")

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

    strategy = json.dumps(
        state["strategy"],
        indent=2,
        ensure_ascii=False,
    )

    review_metrics = json.dumps(
        state["review_metrics"],
        indent=2,
        ensure_ascii=False,
    )

    sales_metrics = json.dumps(
        state["sales_metrics"],
        indent=2,
        ensure_ascii=False,
    )

    inventory_metrics = json.dumps(
        state["inventory_metrics"],
        indent=2,
        ensure_ascii=False,
    )

    prompt = load_prompt(
        "executive_report_agent.j2",
        business_name=state["business_name"],
        review_analysis=review_analysis,
        sales_analysis=sales_analysis,
        inventory_analysis=inventory_analysis,
        marketing_plan=marketing_plan,
        strategy=strategy,
        generated_date=generated_date,
        review_metrics=review_metrics,
        sales_metrics=sales_metrics,
        inventory_metrics=inventory_metrics,
    )    

    llm = LLMService()

    report = llm.invoke(prompt)

    state["executive_report"] = report

    logger.info("Executive Report Agent finished.")
    logger.info("Executive Report State Keys: %s", list(state.keys()))

    return state