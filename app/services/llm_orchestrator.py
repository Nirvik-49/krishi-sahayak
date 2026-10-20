import os
from typing import Dict, Any, List
from app.services.agent import AgentRouter

class LLMOrchestrator:
    """Orchestrates natural language agricultural queries with tool execution."""

    @staticmethod
    async def process_query(prompt: str) -> Dict[str, Any]:
        query = prompt.lower()
        tool_results = []
        
        # Simple intelligent keyword-to-tool dispatcher for MVP execution
        # (Can be extended with real OpenAI/Anthropic client function calling)
        if "weather" in query or "rain" in query or "temperature" in query or "forecast" in query:
            # Extract location if mentioned
            location = "kathmandu"
            for loc in ["pokhara", "chitwan", "biratnagar", "kathmandu"]:
                if loc in query:
                    location = loc
                    break
            
            weather_data = await AgentRouter.execute_tool("get_weather_forecast", {"location": location})
            tool_results.append({"tool": "get_weather_forecast", "data": weather_data})

        if "price" in query or "market" in query or "rate" in query or "potato" in query or "tomato" in query or "onion" in query or "cauliflower" in query:
            crop = "potato"
            for c in ["tomato", "potato", "onion", "cauliflower"]:
                if c in query:
                    crop = c
                    break
            
            market_data = await AgentRouter.execute_tool("get_market_price", {"crop": crop})
            tool_results.append({"tool": "get_market_price", "data": market_data})

        # If no specific tool matched, provide a general guidance response
        if not tool_results:
            return {
                "status": "success",
                "query": prompt,
                "advisory": "Namaste! I am your KrishiSahayak AI advisor. You can ask me about local weather forecasts or Kalimati wholesale market commodity rates."
            }

        return {
            "status": "success",
            "query": prompt,
            "tool_executions": tool_results,
            "advisory": "Based on the retrieved live data above, plan your harvesting or market sales accordingly to maximize your profit."
        }