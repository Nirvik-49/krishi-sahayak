from fastapi import FastAPI
from app.core.config import settings

app = FastAPI(
    title=settings.APP_NAME,
    description="Agricultural decision-support web app for Nepali smallholder farmers",
    version=settings.VERSION,
    debug=settings.DEBUG,
)


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
