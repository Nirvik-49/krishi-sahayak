import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.services.recommendation import RecommendationService

client = TestClient(app)


def test_health_check():
    """Verify health endpoint is responsive."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_home_page():
    """Verify landing page renders successfully."""
    response = client.get("/")
    assert response.status_code == 200
    assert "KrishiSahayak" in response.text


def test_chat_page():
    """Verify AI chat interface renders successfully."""
    response = client.get("/chat")
    assert response.status_code == 200
    assert "AI Advisor" in response.text


def test_dashboard_page():
    """Verify analytics dashboard renders successfully."""
    response = client.get("/dashboard")
    assert response.status_code == 200
    assert "Agricultural Market & Weather Hub" in response.text


def test_about_page():
    """Verify about project overview page renders successfully."""
    response = client.get("/about")
    assert response.status_code == 200
    assert "About KrishiSahayak" in response.text


def test_recommendation_logic():
    """Test AI crop recommendation advisory service logic."""
    advisory = RecommendationService.get_advisory("Potato Red", 28.5, 15)
    assert advisory["crop"] == "Potato Red"
    assert advisory["risk_assessment"] == "Optimal"
    assert "favorable" in advisory["expert_advisory"]


def test_recommendation_high_rain_risk():
    """Test crop recommendation warning on high rain probability."""
    advisory = RecommendationService.get_advisory("Tomato", 25.0, 80)
    assert advisory["risk_assessment"] == "High"
    assert "Heavy rain probability" in advisory["expert_advisory"]


def test_market_price_api():
    """Test Kalimati wholesale market API endpoint."""
    response = client.get("/api/v1/market-price?crop=potato")
    assert response.status_code == 200
    data = response.json()

    assert data["status"] == "success"
    market_data = data["data"]
    assert "Potato" in market_data["item"]
    assert "avg_price" in market_data
    assert market_data["unit"] == "KG"
