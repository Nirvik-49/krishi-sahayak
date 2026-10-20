import httpx
from typing import Dict, Any

class WeatherService:
    """Service to fetch real-time localized weather forecasts using Open-Meteo API."""
    
    # Coordinates for major farming hubs in Nepal
    LOCATION_COORDS = {
        "kathmandu": {"lat": 27.7172, "lon": 85.3240},
        "pokhara": {"lat": 28.2096, "lon": 83.9856},
        "chitwan": {"lat": 27.5291, "lon": 84.3542},
        "biratnagar": {"lat": 26.4525, "lon": 87.2718},
    }

    @classmethod
    async def get_forecast(cls, location: str = "Kathmandu") -> Dict[str, Any]:
        loc_key = location.lower().strip()
        coords = cls.LOCATION_COORDS.get(loc_key, cls.LOCATION_COORDS["kathmandu"])

        url = "https://api.open-meteo.com/v1/forecast"
        params = {
            "latitude": coords["lat"],
            "longitude": coords["lon"],
            "current_weather": True,
            "daily": ["temperature_2m_max", "temperature_2m_min", "precipitation_probability_max"],
            "timezone": "Asia/Kathmandu"
        }

        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(url, params=params, timeout=5.0)
                response.raise_for_status()
                data = response.json()

                current = data.get("current_weather", {})
                daily = data.get("daily", {})

                return {
                    "location": location.capitalize(),
                    "current_temp_c": current.get("temperature"),
                    "windspeed_kmh": current.get("windspeed"),
                    "rain_probability_pct": daily.get("precipitation_probability_max", [0])[0],
                    "forecast_3day": [
                        {
                            "day": f"Day {i+1}",
                            "temp_max": daily["temperature_2m_max"][i],
                            "temp_min": daily["temperature_2m_min"][i],
                            "rain_chance": f"{daily['precipitation_probability_max'][i]}%"
                        }
                        for i in range(min(3, len(daily.get("temperature_2m_max", []))))
                    ],
                    "status": "live_data"
                }
            except Exception as e:
                # Fallback safeguard if API call drops out
                return {
                    "location": location,
                    "status": "fallback_mock",
                    "error": str(e)
                }