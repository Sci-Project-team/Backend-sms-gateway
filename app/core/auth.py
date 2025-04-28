# app/core/auth.py
import bcrypt
import secrets
from datetime import datetime, timedelta
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, APIKeyHeader
from jose import JWTError, jwt
from app.config import settings
from app.services.storage import StorageService
from app.models.user import UserInDB
from fastapi import Depends, HTTPException, status, Security

# Initialize components
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")
api_key_header = APIKeyHeader(name="X-API-Key", auto_error=False)
storage_service = StorageService()

# Password hashing functions
def get_password_hash(password: str) -> str:
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(plain_password.encode(), hashed_password.encode())

# API key generation
def create_api_key() -> str:
    return secrets.token_urlsafe(32)

# JWT token functions
def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt

# User authentication via JWT token
async def get_current_user(token: str = Depends(oauth2_scheme)) -> UserInDB:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    
    user = await storage_service.get_user_by_username(username)
    if user is None:
        raise credentials_exception
    return user

# API key authentication (for system level access only)
async def validate_api_key(api_key_header: str = Security(api_key_header)):
    if not api_key_header:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, 
            detail="API key required"
        )
    
    # Only allow the master API key
    if api_key_header == settings.API_KEY:
        return api_key_header
    
    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN, 
        detail="Invalid API key"
    )