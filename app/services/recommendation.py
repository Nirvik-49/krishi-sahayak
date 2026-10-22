from typing import Dict, Any


class RecommendationService:
    """Calculates agricultural recommendations based on live conditions."""

    @staticmethod
    def get_advisory(crop: str, temp_c: float, rain_prob: int) -> Dict[str, Any]:
        crop_lower = crop.lower()
        advice = ""
        risk_level = "Low"

        if rain_prob > 50:
            risk_level = "High"
            advice = f"Heavy rain probability ({rain_prob}%) detected. Delay harvesting or fertilizer application for {crop} to prevent crop washout."
        elif temp_c > 30:
            risk_level = "Moderate"
            advice = f"High temperature ({temp_c}°C) requires adequate irrigation for {crop} during early morning or evening hours."
        else:
            risk_level = "Optimal"
            advice = f"Weather conditions are stable and favorable for cultivating and managing {crop}."

        return {
            "crop": crop,
            "current_temperature_c": temp_c,
            "rain_probability_pct": rain_prob,
            "risk_assessment": risk_level,
            "expert_advisory": advice
        }
