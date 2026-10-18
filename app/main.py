from fastapi import FastAPI
from app.core.config import settings
from app.api.v1_endpoints import router as v1_router

app = FastAPI(
    title=settings.APP_NAME,
    description="Agricultural decision-support web app for Nepali smallholder farmers",
    version=settings.VERSION,
    debug=settings.DEBUG,
)

# Register API routes
app.include_router(v1_router)


@app.get("/")
async def root():
    return {
        "status": "online",
        "service": settings.APP_NAME,
        "version": settings.VERSION,
        "message": "Namaste! कृषि-सहायक API is running."
    }


@app.get("/health")
async def health_check():
    return {"status": "healthy"}
