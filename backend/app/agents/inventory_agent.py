import json

from app.core.logging import logger
from app.graph.state import BusinessState
from app.services.llm import LLMService
from app.services.metrics import build_inventory_intelligence
from app.tools.prompt_loader import load_prompt
from app.tools.inventory_loader import load_inventory


def inventory_agent(state: BusinessState) -> BusinessState:
    """
    Analyze inventory data using Gemini.
    """

    logger.info("Inventory Agent started.")

    inventory = load_inventory()
    intelligence = build_inventory_intelligence(inventory)

    prompt = load_prompt(
        "inventory_agent.j2",
        business_name=state["business_name"],
        inventory_metrics=intelligence,
    )

    llm = LLMService()

    analysis = llm.invoke_json(prompt)

    state["inventory"] = inventory
    state["inventory_metrics"] = intelligence
    state["inventory_analysis"] = analysis
    state.pop("inventory", None)

    logger.info("Inventory Agent finished.")

    return state