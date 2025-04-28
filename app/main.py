import logging
from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from app.api.routes import sms, auth
from app.services.storage import StorageService
from app.services.gsm_service import GSMService
from app.utils.logger import setup_logging
from app.config import settings
from dotenv import load_dotenv
from app.api.routes import sms, auth, admin
load_dotenv()

# Create services
storage_service = StorageService()
gsm_service = GSMService(storage_service)

# Setup logging
setup_logging(storage_service)
logger = logging.getLogger(__name__)

# Define lifespan context manager for startup and shutdown events
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup event logic
    logger.info("SMS Gateway API starting up")
    # Initialize any services or hardware here
    yield
    # Shutdown event logic
    logger.info("SMS Gateway API shutting down")
    # Clean up resources or close connections here

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

@app.get("/")
async def root():
    """
    Root endpoint to check if the API is running
    """
    logger.info("Root endpoint accessed")
    return {"status": "online", "version": "1.0.0"}
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)