# app/api/routes/admin.py
from fastapi import APIRouter, Depends, HTTPException
from typing import List, Dict, Any
from app.services.storage import StorageService
from app.core.auth import get_current_user, validate_api_key
from fastapi import Security

router = APIRouter()
storage_service = StorageService()

@router.get("/users", response_model=List[Dict[str, Any]])
async def list_users(api_key: str = Security(validate_api_key)):
    """
    List all users in the database (admin only)
    """
    users = await storage_service.get_all_users()
    return users

@router.get("/messages", response_model=List[Dict[str, Any]])
async def list_messages(api_key: str = Security(validate_api_key)):
    """
    List all messages in the database (admin only)
    """
    messages = await storage_service.get_all_messages()
    return messages