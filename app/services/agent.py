import json
from typing import Dict, Any, List
from app.services.weather import WeatherService
from app.services.market import MarketService

# Tool definitions structured for OpenAI / Open-Weight LLM Function Calling
TOOLS_SCHEMA = [
    {
        "type": "function",
        "function": {
            "name": "get_weather_forecast",
            "description": "Fetch real-time localized weather forecasts and rain probability in Nepal.",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "City or region in Nepal (e.g. Kathmandu, Pokhara, Chitwan, Biratnagar)"
                    }
                },
                "required": ["location"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_market_price",
            "description": "Fetch latest daily wholesale commodity market rates from Kalimati Market.",
            "parameters": {
                "type": "object",
                "properties": {
                    "crop": {
                        "type": "string",
                        "description": "Name of the crop/vegetable in English (e.g. tomato, potato, onion, cauliflower)"
                    }
                },
                "required": ["crop"]
            }
        }
    }
]


class AgentRouter:
    """Tool execution engine for processing agent decision calls."""

    @staticmethod
    async def execute_tool(tool_name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        if tool_name == "get_weather_forecast":
            location = arguments.get("location", "Kathmandu")
            return await WeatherService.get_forecast(location)

        elif tool_name == "get_market_price":
            crop = arguments.get("crop", "potato")
            return await MarketService.get_price(crop)

        return {"error": f"Tool '{tool_name}' is not supported."}
