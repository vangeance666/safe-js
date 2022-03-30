
from app.routers.api_v1_0 import router as api_v1_0_router
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

templates = Jinja2Templates(directory="app/templates")
app.mount("/static", StaticFiles(directory="app/static"), name="static")

app.include_router(api_v1_0_router, tags=["api"], prefix="/api/v1_0")

@app.get('/heartbeat/')
async def heartbeat():
	return JSONResponse(content={"status": "healthy"})

@app.get('/')
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

