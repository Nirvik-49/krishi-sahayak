from fastapi import FastAPI

app = FastAPI(
    title="KrishiSahayak API",
    description="Agricultural decision-support web app for Nepali smallholder farmers",
    version="0.1.0",
)


@app.get("/")
async def root():
    return {
        "status": "online",
        "service": "KrishiSahayak Backend",
        "message": "Namaste! कृषि-सहायक API is running."
    }


@app.get("/health")
async def health_check():
    return {"status": "healthy"}
