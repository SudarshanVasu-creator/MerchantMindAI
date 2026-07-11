from typing import Any, TypeAlias, TypedDict

JSONDict: TypeAlias = dict[str, Any]
JSONList: TypeAlias = list[JSONDict]


class BusinessState(TypedDict):
    """
    Shared state passed between all LangGraph nodes.
    """

    # Business information
    business_name: str

    # Input datasets
    reviews: JSONList
    sales: JSONList
    inventory: JSONList

    # Agent outputs
    review_analysis: JSONDict
    sales_analysis: JSONDict
    inventory_analysis: JSONDict
    marketing_plan: JSONDict
    strategy: JSONDict

    # Final output
    executive_report: str