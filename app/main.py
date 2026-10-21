from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.core.config import settings
from app.api.v1_endpoints import router as v1_router

app = FastAPI(
    title=settings.APP_NAME,
    description="Agricultural decision-support web app for Nepali smallholder farmers",
    version=settings.VERSION,
    debug=settings.DEBUG,
)

# Static and Template Setup
app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

# Register API routes
app.include_router(v1_router)


@app.get("/", response_class=HTMLResponse)
async def serve_home(request: Request):
    """Serve home page HTML dashboard."""
    return templates.TemplateResponse(
        request,             # 1st argument: Request object
        "index.html",        # 2nd argument: Template file name
        {"title": settings.APP_NAME}  # 3rd argument: Context dictionary
    )


@app.get("/health")
async def health_check():
    return {"status": "healthy"}


@app.get("/chat", response_class=HTMLResponse)
async def serve_chat(request: Request):
    """Serve the AI Assistant Chat interface."""
    return templates.TemplateResponse(
        request,
        "chat.html",
        {"title": settings.APP_NAME}
    )
