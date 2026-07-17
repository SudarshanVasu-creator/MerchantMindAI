from fastapi import APIRouter

from app.graph.workflow import build_graph

router = APIRouter(prefix="/workflow", tags=["Workflow"])


@router.get("/test")
def test_workflow():

    graph = build_graph()

    result = graph.invoke(
        {
            "business_name": "Sunrise Café",

            # Raw Data
            "reviews": [],
            "sales": [],
            "inventory": [],

            # Deterministic Metrics
            "review_intelligence": {},
            "sales_metrics": {},
            "inventory_metrics": {},

            # AI Analysis
            "review_analysis": {},
            "sales_analysis": {},
            "inventory_analysis": {},

            # Strategic Outputs
            "marketing_plan": {},
            "strategy": {},

            # Final Report
            "executive_report": "",
        }
    )

    return result