# app/config.py
import os
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # API settings
    API_KEY: str = os.getenv("API_KEY", "default_api_key_for_development")
    SECRET_KEY: str = os.getenv("SECRET_KEY", "very_secret_key_for_development")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7  # 7 days
    
    # GSM settings
    GSM_PORT: str = os.getenv("GSM_PORT", "/dev/ttyUSB0")
    GSM_BAUDRATE: int = int(os.getenv("GSM_BAUDRATE", "9600"))
    GSM_PIN: str = os.getenv("GSM_PIN", "")
    
    # Development/Production flag
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "development")
    
    # Simulation mode flag (added)
    SIMULATION_MODE: bool = os.getenv("SIMULATION_MODE", "False").lower() == "true"
    
    class Config:
        env_file = ".env"

settings = Settings()
