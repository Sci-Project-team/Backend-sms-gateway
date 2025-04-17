import os
from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    API_KEY: str = "test_api_key"
    GSM_PORT: str = "COM3"  
    GSM_BAUDRATE: int = 9600
    SIMULATION_MODE: bool = True

    class Config:
        env_file = ".env"

settings = Settings()
