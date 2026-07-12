from langgraph.graph import END, START, StateGraph

from app.graph.nodes import chief_business_officer
from app.graph.state import BusinessState
from app.agents.review_agent import review_agent
from app.agents.sales_agent import sales_agent
from app.agents.inventory_agent import inventory_agent


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
        END,
    )

    return workflow.compile()