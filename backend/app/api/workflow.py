from fastapi import APIRouter

from app.graph.workflow import build_graph

router = APIRouter(prefix="/workflow", tags=["Workflow"])


@router.get("/test")
def test_workflow():

    graph = build_graph()

    result = graph.invoke(
        {
            "business_name": "Demo Bakery",
            "reviews": [],
            "sales": [],
            "inventory": [],
            "review_analysis": {},
            "sales_analysis": {},
            "inventory_analysis": {},
            "marketing_plan": {},
            "strategy": {},
            "executive_report": "",
        }
    )

    return result