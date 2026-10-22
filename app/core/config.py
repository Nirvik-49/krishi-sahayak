import os
from pydantic_settings import BaseSettings
from pydantic import ConfigDict


class Settings(BaseSettings):
    APP_NAME: str = "KrishiSahayak"
    DEBUG: bool = True
    VERSION: str = "0.1.0"

    # API Keys for Build Phase integrations
    OPENAI_API_KEY: str = ""
    WEATHER_API_KEY: str = ""

    model_config = ConfigDict(
        env_file=".env",
        extra="ignore"
    )


settings = Settings()
