from langgraph.graph import END, START, StateGraph

from app.graph.nodes import chief_business_officer
from app.graph.state import BusinessState


def build_graph():

    workflow = StateGraph(BusinessState)

    workflow.add_node(
        "chief_business_officer",
        chief_business_officer,
    )

    workflow.add_edge(
        START,
        "chief_business_officer",
    )

    workflow.add_edge(
        "chief_business_officer",
        END,
    )

    return workflow.compile()