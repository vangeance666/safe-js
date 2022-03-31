from fastapi import APIRouter, Body
from fastapi.responses import JSONResponse

from app.models.analysis_request import AnalysisRequest

router = APIRouter()


@router.get("/analysis/statistics/")
async def get_dashboard_stats():
    return JSONResponse(content={"no_of_tasks": 2, "analyzed_count": 5})


@router.get("/analysis/results/")
async def get_past_results():
    return JSONResponse(content={
        "status": "ok", "headers": ["Page URL", "JS Src", "Static analysis Status", "Dynamic analysis Status", "Prediction"], "rows": [
            ["www.facebook.com", 'jomama source', 'Done', 'Done', '50']
        ]}
    )


@router.post("/analysis/run/")
async def analyze_url(analysis_request: AnalysisRequest = Body(...)):
    # Add analysis to queue and return analysis id
    return JSONResponse(content={"status": "ok", "task_id": 1})


@router.get("/analysis/run/status/")
async def analysis_status(id: int = 0):
    # Pending|Running|Done
    return JSONResponse(content={"status": "found", "task_status": "Pending", "task_id": 1})
