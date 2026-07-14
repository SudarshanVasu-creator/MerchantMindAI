import json

from app.core.logging import logger
from app.graph.state import BusinessState
from app.services.llm import LLMService
from app.services.metrics import calculate_inventory_metrics
from app.tools.prompt_loader import load_prompt
from app.tools.inventory_loader import load_inventory


def inventory_agent(state: BusinessState) -> BusinessState:
    """
    Analyze inventory data using Gemini.
    """

    logger.info("Inventory Agent started.")

    inventory = load_inventory()
    metrics = calculate_inventory_metrics(inventory)

    inventory_json = json.dumps(
        inventory,
        indent=2,
        ensure_ascii=False,
    )
    prompt = load_prompt(
        "inventory_agent.j2",
        business_name=state["business_name"],
        inventory=inventory_json,
    )

    llm = LLMService()

    analysis = llm.invoke_json(prompt)

    state["inventory"] = inventory
    state["inventory_metrics"] = metrics
    state["inventory_analysis"] = analysis

    logger.info("Inventory Agent finished.")

    return state