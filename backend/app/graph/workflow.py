from langgraph.graph import END, START, StateGraph

from app.graph.nodes import chief_business_officer
from app.graph.state import BusinessState
from app.agents.review_agent import review_agent
from app.agents.sales_agent import sales_agent
from app.agents.inventory_agent import inventory_agent
from app.agents.marketing_agent import marketing_agent
from app.agents.strategy_agent import strategy_agent
from app.agents.executive_report_agent import executive_report_agent


def build_graph():

    workflow = StateGraph(BusinessState)

    workflow.add_node(
        "chief_business_officer",
        chief_business_officer,
    )
    
    workflow.add_node(
        "review_agent",
        review_agent,
    )

    workflow.add_node(
        "sales_agent",
        sales_agent,
    )

    workflow.add_node(
        "inventory_agent",
        inventory_agent,
    )

    workflow.add_node(
        "marketing_agent",
        marketing_agent,
    )

    workflow.add_node(
        "strategy_agent",
        strategy_agent,
    )

    workflow.add_node(
        "executive_report_agent",
        executive_report_agent,
    )

    workflow.add_edge(
        START,
        "chief_business_officer",
    )

    workflow.add_edge(
        "chief_business_officer",
        "review_agent",
    )

    workflow.add_edge(
        "review_agent",
        "sales_agent",
    )

    workflow.add_edge(
        "sales_agent",
        "inventory_agent",
    )
    
    workflow.add_edge(
        "inventory_agent",
        "marketing_agent",
    )

    workflow.add_edge(
        "marketing_agent",
        "strategy_agent",
    )

    workflow.add_edge(
        "strategy_agent",
        "executive_report_agent",
    )

    workflow.add_edge(
        "executive_report_agent",
        END,
    )

    return workflow.compile()