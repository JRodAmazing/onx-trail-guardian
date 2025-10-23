"""Core application configuration."""

from functools import lru_cache
from typing import List
from pydantic_settings import BaseSettings
from pydantic import Field, validator


class Settings(BaseSettings):
    """Application settings from environment variables."""
    
    # Application
    APP_NAME: str = "Trail Guardian Pro"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = False
    ENVIRONMENT: str = "development"
    API_V1_PREFIX: str = "/api/v1"
    SECRET_KEY: str = Field(..., min_length=32)
    
    # Database
    DATABASE_URL: str = "postgresql://postgres:postgres@localhost:5432/trailguardian"
    
    # Redis
    REDIS_URL: str = "redis://localhost:6379/0"
    CELERY_BROKER_URL: str = "redis://localhost:6379/1"
    
    # API Keys
    FIRMS_API_KEY: str = ""
    MAPBOX_ACCESS_TOKEN: str = ""
    NOAA_API_KEY: str = ""
    OPENAI_API_KEY: str = ""
    
    # AWS
    AWS_ACCESS_KEY_ID: str = ""
    AWS_SECRET_ACCESS_KEY: str = ""
    AWS_S3_BUCKET: str = ""
    AWS_REGION: str = "us-west-2"
    
    # CORS
    CORS_ORIGINS: List[str] = ["http://localhost:3000"]
    
    # Threat Scoring Weights
    THREAT_WEIGHT_FIRE_PROXIMITY: float = 0.35
    THREAT_WEIGHT_FIRE_BEHAVIOR: float = 0.25
    THREAT_WEIGHT_WEATHER: float = 0.20
    THREAT_WEIGHT_TERRAIN: float = 0.15
    THREAT_WEIGHT_HISTORICAL: float = 0.05
    
    # Distance thresholds (meters)
    CRITICAL_FIRE_DISTANCE: int = 5000
    WARNING_FIRE_DISTANCE: int = 15000
    WATCH_FIRE_DISTANCE: int = 30000
    
    class Config:
        env_file = ".env"
        case_sensitive = True
    
    @validator("CORS_ORIGINS", pre=True)
    def parse_cors_origins(cls, v):
        if isinstance(v, str):
            return [origin.strip() for origin in v.split(",")]
        return v


@lru_cache()
def get_settings() -> Settings:
    """Get cached settings instance."""
    return Settings()


settings = get_settings()
