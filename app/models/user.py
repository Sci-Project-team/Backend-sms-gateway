# app/models/user.py
from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime
import uuid

class UserBase(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    email: EmailStr
    full_name: Optional[str] = None

class UserCreate(UserBase):
    password: str = Field(..., min_length=8)

class UserInDB(UserBase):
    id: str
    hashed_password: str
    api_key: str
    created_at: datetime
    is_active: bool = True

class UserResponse(UserBase):
    id: str
    api_key: str
    created_at: datetime
    is_active: bool