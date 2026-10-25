from fastapi import APIRouter, Query
from pydantic import BaseModel
from typing import Dict, Any
from app.services.weather import WeatherService
from app.services.market import MarketService
from app.services.agent import AgentRouter, TOOLS_SCHEMA
from app.services.recommendation import RecommendationService

# Note: Prefix is handled in main.py via include_router to avoid double prefixing (/api/v1/api/v1)
router = APIRouter(tags=["Agricultural Services"])


class ToolCallRequest(BaseModel):
    tool_name: str
    arguments: Dict[str, Any]


class AgentQueryRequest(BaseModel):
    prompt: str


@router.get("/weather")
async def fetch_weather(location: str = Query(default="Kathmandu", description="Location name in Nepal")):
    """Get localized weather predictions for harvesting decisions."""
    return await WeatherService.get_forecast(location)


@router.get("/market-price")
async def fetch_market_price(crop: str = Query(..., description="Crop name e.g. tomato, potato, onion")):
    """Get latest Kalimati wholesale commodity prices."""
    return await MarketService.get_price(crop)


@router.get("/agent/tools")
async def get_agent_tools():
    """Retrieve available tool declarations for LLM function calling."""
    return {"tools": TOOLS_SCHEMA}


@router.post("/agent/execute")
async def execute_agent_tool(request: ToolCallRequest):
    """Execute tool calls routed from LLM responses."""
    result = await AgentRouter.execute_tool(request.tool_name, request.arguments)
    return {"status": "success", "tool_name": request.tool_name, "output": result}


@router.post("/agent/query")
async def query_agricultural_agent(request: AgentQueryRequest):
    """Process natural language farming queries using the tool-execution engine."""
    from app.services.llm_orchestrator import LLMOrchestrator
    return await LLMOrchestrator.process_query(request.prompt)


@router.get("/recommendation")
async def get_crop_recommendation(
    crop: str = Query(default="potato", description="Crop name"),
    temperature: float = Query(
        default=25.0, description="Current temperature in Celsius"),
    rain_probability: int = Query(
        default=10, description="Rain probability percentage")
):
    """Generate smart agricultural risk and management advisory."""
    return RecommendationService.get_advisory(crop, temperature, rain_probability)
