from fastapi import APIRouter, Query
from app.services.weather import WeatherService
from app.services.market import MarketService

router = APIRouter(prefix="/api/v1", tags=["Agricultural Services"])


@router.get("/weather")
async def fetch_weather(location: str = Query(default="Kathmandu", description="Location name in Nepal")):
    """Get localized weather predictions for harvesting decisions."""
    return await WeatherService.get_forecast(location)


@router.get("/market-price")
async def fetch_market_price(crop: str = Query(..., description="Crop name e.g. tomato, potato, onion")):
    """Get latest Kalimati wholesale commodity prices."""
    return await MarketService.get_price(crop)
