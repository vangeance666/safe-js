from fastapi import APIRouter, Body
from fastapi.responses import JSONResponse

from app.models.analysis_request import AnalysisRequest

from app.platform_controller import PlatformController

platform_controller = PlatformController()

router = APIRouter()


test_headers = ["ID", "Page URL", "JS Src", "Static analysis Status", "Dynamic analysis Status"]
test_data_rows = [
            [str(x), "www.facebook.com", 'jomama source', 'Done', 'Done'] for x in range(100)
        ]

# test_analysis_headers = 
# Used for dashboard view

# Done
@router.get("/analysis/statistics/")
async def get_dashboard_stats():
    try:
        return JSONResponse(content={"status": "ok"
            , "details": platform_controller.fetch_dashboard_details()})
    except Exception as e:
        return JSONResponse(content={"status": "error", "error_message": str(e)})

# Used for recent view
@router.get("/analysis/overview/")
async def get_analysis_overview():
    try:
        return JSONResponse(content={"status": "ok"
            , "details": platform_controller.fetch_all_pages_details()})
    except Exception as e:
        return JSONResponse(content={"status": "error", "error_message": str(e)})        
        
# Done
@router.get("/analysis/details/")
async def get_analysis_details(page_id: int, js_file_id: int):
    try:
        return JSONResponse(content={"status": "ok", "details": platform_controller.fetch_js_file_details(page_id, js_file_id)})
    except Exception as e:
        return JSONResponse(content={"status": "error", "error_message": str(e)})
    
    # return JSONResponse(content={"testing":"yes"})

# use for submitting samples from extension/site
@router.post("/analysis/run/")
async def analyze_url(analysis_request: AnalysisRequest = Body(...)):
    # Add analysis to queue and return analysis id
    return JSONResponse(content={"status": "ok", "task_id": 1})

# Used for querying status for both extension/site
@router.get("/analysis/run/status/")
async def analysis_status(id: int = 0):
    # Pending|Running|Done
    return JSONResponse(content={"status": "found", "task_status": "Pending", "task_id": 1})
