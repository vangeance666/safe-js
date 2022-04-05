import atexit
import signal

from app.controllers import platform_controller
from app.models.analysis_request import AnalysisRequest
from fastapi import APIRouter, Body
from fastapi.responses import JSONResponse

router = APIRouter()

# Done
@router.get("/analysis/statistics/")
async def get_dashboard_stats():
    try:
        return JSONResponse(content={"status": "ok", "details": platform_controller.fetch_dashboard_details()})
    except Exception as e:
        return JSONResponse(content={"status": "error", "error_message": str(e)})


@router.get("/analysis/pending/")
async def get_analysis_pending():
    try:
        return JSONResponse(content={"status": "ok", "details": platform_controller.fetch_pending_details()})
    except Exception as e:
        return JSONResponse(content={"status": "error", "error_message": str(e)})

# Used for recent view


@router.get("/analysis/overview/")
async def get_analysis_overview():
    try:
        return JSONResponse(content={"status": "ok", "details": platform_controller.fetch_all_pages_details()})
    except Exception as e:
        return JSONResponse(content={"status": "error", "error_message": str(e)})

# Done


@router.get("/analysis/details/")
async def get_analysis_details(page_id: int, js_file_id: int):
    try:
        js_file_details = platform_controller.fetch_js_file_details(
            page_id, js_file_id)
        if not js_file_details:
            return JSONResponse(content={"status": "no-record"})

        return JSONResponse(content={"status": "ok", "details": js_file_details})
    except Exception as e:
        return JSONResponse(content={"status": "error", "error_message": str(e)})

    # return JSONResponse(content={"testing":"yes"})

# use for submitting samples from extension/site


@router.post("/analysis/run/")
async def analyze_url(analysis_request: AnalysisRequest = Body(...)):
    try:
        if analysis_request.mode == "single":
            print("API Executing single mode")
            return JSONResponse(content={"status": "ok", "page_id": platform_controller.analyze_one_url(analysis_request.url), "url": analysis_request.url})

        return JSONResponse(content={"status": "error", "error_message": "Invalid Mode"})
    except Exception as e:
        return JSONResponse(content={"status": "error", "error_message": str(e)})


# Used for querying status for both extension/site
@router.get("/analysis/run/status/")
async def analysis_status(id: int = 0):
    # Pending|Running|Done
    return JSONResponse(content={"status": "found", "task_status": "Pending", "task_id": 1})


@router.get('/analysis/reset/')
async def clear_all_data():
    try:
        if not platform_controller.delete_past_data():
            return JSONResponse(content={"status": "fail"})
        return JSONResponse(content={"status": "ok"})
    except Exception as e:
        return JSONResponse(content={"status": "error", "error_message": str(e)})


@router.get('/analysis/save/')
async def save_data():
    try:
        platform_controller.cleanup()
        return JSONResponse(content={"status": "ok"})
    except Exception as e:
        return JSONResponse(content={"status": "error", "error_message": str(e)})
