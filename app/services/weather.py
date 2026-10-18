import httpx
from typing import Dict, Any


class WeatherService:
    """Service to fetch localized weather forecasts for agricultural planning."""

    @staticmethod
    async def get_forecast(location: str = "Kathmandu") -> Dict[str, Any]:
        # Placeholder logic returning structured schema for LLM tool integration
        # Can be swapped with Open-Meteo or OpenWeatherMap API calls
        return {
            "location": location,
            "current_temp_c": 22.5,
            "condition": "Partly Cloudy",
            "rain_probability_pct": 15,
            "forecast_3day": [
                {"day": "Tomorrow", "condition": "Sunny", "rain_chance": "10%"},
                {"day": "Day 2", "condition": "Light Rain", "rain_chance": "60%"},
                {"day": "Day 3", "condition": "Thunderstorm", "rain_chance": "80%"}
            ],
            "harvest_risk": "Moderate rain risk predicted in 48 hours."
        }
