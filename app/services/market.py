from typing import Dict, Any


class MarketService:
    """Service to fetch real-time wholesale produce prices (Kalimati Market)."""

    MOCK_PRICES = {
        "tomato": {"item": "Tomato Small (टमाटर लहान)", "unit": "KG", "min_price": 40, "max_price": 50, "avg_price": 45},
        "potato": {"item": "Potato Red (आलु रातो)", "unit": "KG", "min_price": 55, "max_price": 65, "avg_price": 60},
        "cauliflower": {"item": "Cauliflower Local (काउली स्थानीय)", "unit": "KG", "min_price": 70, "max_price": 85, "avg_price": 78},
        "onion": {"item": "Onion Dry (प्याज सुकेको)", "unit": "KG", "min_price": 80, "max_price": 90, "avg_price": 85},
    }

    @classmethod
    async def get_price(cls, crop_name: str) -> Dict[str, Any]:
        key = crop_name.lower().strip()
        if key in cls.MOCK_PRICES:
            return {"status": "success", "data": cls.MOCK_PRICES[key]}

        return {
            "status": "not_found",
            "message": f"Price data for '{crop_name}' is currently unavailable at Kalimati market."
        }
