# app/main.py
import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os

from app.api.routes import sms, auth, admin
from app.services.storage import StorageService
from app.services.gsm_service import GSMService
from .mqtt_service import MQTTService
from app.utils.logger import setup_logging

# Load environment variables
load_dotenv()

# Global variables for services (will be initialized in lifespan)
storage_service = None
mqtt_service = None
gsm_service = None

logger = logging.getLogger(__name__)

# Define lifespan context manager for startup and shutdown events
@asynccontextmanager
async def lifespan(app: FastAPI):
    global storage_service, mqtt_service, gsm_service
    
    logger.info("SMS Gateway API starting up")
    
    # Initialize storage service first
    storage_service = StorageService()
    setup_logging(storage_service)
    
    # Create and start MQTT service
    mqtt_service = MQTTService(
        broker=os.getenv("MQTT_BROKER", "broker.emqx.io"),
        port=int(os.getenv("MQTT_PORT", "1883")),
        username=os.getenv("MQTT_USERNAME", "emqx"),
        password=os.getenv("MQTT_PASSWORD", "public")
    )
    
    try:
        mqtt_service.start()
        logger.info("MQTT service started successfully")
    except Exception as e:
        logger.error(f"Failed to start MQTT service: {e}")
    
    # NOW create GSM service with the initialized MQTT service
    gsm_service = GSMService(storage_service, mqtt_service)
    logger.info("GSM service initialized with MQTT service")
    
    # Store services in app state for route access
    app.state.storage_service = storage_service
    app.state.mqtt_service = mqtt_service
    app.state.gsm_service = gsm_service
    
    yield
    
    # Shutdown services
    try:
        if mqtt_service:
            mqtt_service.stop()
            logger.info("MQTT service stopped successfully")
    except Exception as e:
        logger.error(f"Error stopping MQTT service: {e}")
    
    logger.info("SMS Gateway API shutting down")

# Initialize FastAPI app with lifespan
app = FastAPI(
    title="SMS Gateway API",
    description="API for sending and receiving SMS through a GSM module",
    version="1.0.0",
    lifespan=lifespan
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router, prefix="/auth", tags=["authentication"])
app.include_router(sms.router, tags=["SMS"])
app.include_router(admin.router, prefix="/admin", tags=["admin"])

# Root endpoint with service status
@app.get("/")
async def root():
    logger.info("Root endpoint accessed")
    return {
        "status": "online", 
        "version": "1.0.0",
        "mqtt_connected": mqtt_service.is_running if mqtt_service else False,
        "services_initialized": all([storage_service, mqtt_service, gsm_service])
    }

# Debug endpoint to check service status
@app.get("/debug/services")
async def debug_services():
    return {
        "storage_service": storage_service is not None,
        "mqtt_service": {
            "initialized": mqtt_service is not None,
            "running": mqtt_service.is_running if mqtt_service else False,
            "thread_alive": mqtt_service.thread.is_alive() if mqtt_service and mqtt_service.thread else False
        },
        "gsm_service": {
            "initialized": gsm_service is not None,
            "has_mqtt_reference": gsm_service.mqtt_service is not None if gsm_service else False
        }
    }

# Entry point when running directly
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
