# app/api/routes/auth.py
from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta


from pydantic import BaseModel

from app.models.user import UserCreate, UserResponse
from app.core.auth import get_password_hash, verify_password, create_api_key, create_access_token
from app.services.storage import StorageService
from app.config import settings

router = APIRouter()
storage_service = StorageService()

@router.post("/register", response_model=UserResponse)
async def register(user: UserCreate):
    """
    Create a new user with generated API key
    """
    try:
        # Check if username already exists
        existing_user = await storage_service.get_user_by_username(user.username)
        if existing_user:
            raise HTTPException(status_code=400, detail="Username already registered")
            
        hashed_password = get_password_hash(user.password)
        api_key = create_api_key()
        
        user_in_db = await storage_service.create_user(user, hashed_password, api_key)
        
        return UserResponse(
            id=user_in_db.id,
            username=user_in_db.username,
            email=user_in_db.email,
            full_name=user_in_db.full_name,
            api_key=user_in_db.api_key,
            created_at=user_in_db.created_at,
            is_active=user_in_db.is_active
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to register user: {str(e)}")

# Login endpoint using OAuth2 form - this matches the OAuth2PasswordBearer tokenUrl
@router.post("/login", response_model=dict)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await storage_service.get_user_by_username(form_data.username)
    
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password"
        )
    
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    
    return {"access_token": access_token, "token_type": "bearer"}