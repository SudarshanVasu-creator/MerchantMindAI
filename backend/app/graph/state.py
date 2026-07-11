from typing import Any, Dict, List, TypedDict


class BusinessState(TypedDict):
    """
    Shared state passed between all LangGraph nodes.
    """

    # Business information
    business_name: str

    # Input datasets
    reviews: List[Dict[str, Any]]
    sales: List[Dict[str, Any]]
    inventory: List[Dict[str, Any]]

    # Agent outputs
    review_analysis: Dict[str, Any]
    sales_analysis: Dict[str, Any]
    inventory_analysis: Dict[str, Any]
    marketing_plan: Dict[str, Any]
    strategy: Dict[str, Any]

    # Final output
    executive_report: str