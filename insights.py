from fastapi import APIRouter, Request
from ai.insight_engine import generate_insights

router = APIRouter()

@router.post("/analyze")
async def analyze(request: Request):
    data = await request.json()
    insights = generate_insights(data["visual_data"])
    return {
        "summary": insights["summary"],
        "recommendations": insights["recommendations"]
    }