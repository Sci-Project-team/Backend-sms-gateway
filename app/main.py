# app/main.py
import logging
from contextlib import asynccontextmanager
import os
from dotenv import load_dotenv

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

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
    logger.info("Storage service initialized")
    
    # Create MQTT service
    mqtt_service = MQTTService(
        broker=os.getenv("MQTT_BROKER", "broker.emqx.io"),
        port=int(os.getenv("MQTT_PORT", "1883")),
        username=os.getenv("MQTT_USERNAME", "emqx"),
        password=os.getenv("MQTT_PASSWORD", "public")
    )
    
    # IMPORTANT: Set storage service BEFORE starting MQTT
    mqtt_service.set_storage_service(storage_service)
    logger.info("Storage service set for MQTT service")
    
    # Create GSM service with MQTT dependency
    gsm_service = GSMService(storage_service, mqtt_service)
    logger.info("GSM service initialized with MQTT service")
    
    # Start MQTT service AFTER setting storage service
    try:
        mqtt_service.start()
        logger.info("MQTT service started successfully")
        
        # Verify MQTT service is running
        if mqtt_service.is_running:
            logger.info("MQTT service confirmed running")
        else:
            logger.warning("MQTT service started but not confirmed running")
            
    except Exception as e:
        logger.error(f"Failed to start MQTT service: {e}")
    
    # Store services in app state for route access
    app.state.storage_service = storage_service
    app.state.mqtt_service = mqtt_service
    app.state.gsm_service = gsm_service
    
    yield
    
    # Cleanup logging before shutdown
    db_handler = None
    for handler in logging.getLogger().handlers:
        if hasattr(handler, 'close') and hasattr(handler, 'log_queue'):
            db_handler = handler
            break
    
    if db_handler:
        db_handler.close()
        logger.info("Database logging handler closed")
    
    # Shutdown MQTT service
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

# Debug endpoints
@app.get("/debug/services")
async def debug_services():
    """Debug endpoint to check service status"""
    return {
        "storage_service": storage_service is not None,
        "mqtt_service": {
            "initialized": mqtt_service is not None,
            "running": mqtt_service.is_running if mqtt_service else False,
            "thread_alive": mqtt_service.thread.is_alive() if mqtt_service and mqtt_service.thread else False,
            "storage_service_set": mqtt_service.storage_service is not None if mqtt_service else False
        },
        "gsm_service": {
            "initialized": gsm_service is not None,
            "has_mqtt_reference": gsm_service.mqtt_service is not None if gsm_service else False
        }
    }

@app.get("/debug/mqtt-status")
async def mqtt_status():
    """Debug endpoint to check MQTT service status"""
    if not mqtt_service:
        return {"status": "not_initialized", "running": False}
    
    return {
        "status": "initialized",
        "running": mqtt_service.is_running,
        "broker": mqtt_service.broker,
        "port": mqtt_service.port,
        "thread_alive": mqtt_service.thread.is_alive() if mqtt_service.thread else False,
        "storage_service_available": mqtt_service.storage_service is not None
    }

@app.get("/debug/mqtt-storage")
async def debug_mqtt_storage():
    """Check if MQTT service has storage service"""
    if mqtt_service:
        return {
            "mqtt_service_exists": True,
            "storage_service_set": mqtt_service.storage_service is not None,
            "storage_service_type": type(mqtt_service.storage_service).__name__ if mqtt_service.storage_service else None
        }
    return {"mqtt_service_exists": False}

@app.get("/debug/all-messages")
async def get_all_messages():
    """Debug endpoint to see all messages"""
    import sqlite3
    
    try:
        conn = sqlite3.connect('data/sms_gateway.db')
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM messages ORDER BY created_at DESC LIMIT 50")
        messages = cursor.fetchall()
        
        # Get column names
        columns = [description[0] for description in cursor.description]
        
        # Convert to list of dictionaries
        result = []
        for msg in messages:
            result.append(dict(zip(columns, msg)))
        
        conn.close()
        return {"total": len(result), "messages": result}
    except Exception as e:
        return {"error": str(e)}

@app.get("/debug/db-structure")
async def check_db_structure():
    """Check database structure"""
    import sqlite3
    
    try:
        conn = sqlite3.connect('data/sms_gateway.db')
        cursor = conn.cursor()
        
        # Check if messages table exists
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='messages';")
        table_exists = cursor.fetchone() is not None
        
        # Get table schema
        cursor.execute("PRAGMA table_info(messages);")
        columns = cursor.fetchall()
        
        # Count total messages
        cursor.execute("SELECT COUNT(*) FROM messages;")
        total_count = cursor.fetchone()[0]
        
        # Count by direction
        cursor.execute("SELECT direction, COUNT(*) FROM messages GROUP BY direction;")
        direction_counts = cursor.fetchall()
        
        conn.close()
        
        return {
            "table_exists": table_exists,
            "columns": columns,
            "total_messages": total_count,
            "direction_counts": dict(direction_counts)
        }
    except Exception as e:
        return {"error": str(e)}

# Entry point when running directly
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
