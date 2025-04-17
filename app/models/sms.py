from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime
from enum import Enum

class SmsStatus(str, Enum):
    PENDING = "pending"
    SENT = "sent"
    FAILED = "failed"
    RECEIVED = "received"

class SmsBase(BaseModel):
    phone_number: str = Field(description="Le numéro de téléphone complet avec indicatif")
    message: str = Field(description="Le contenu du message SMS")

class SmsCreate(SmsBase):
    pass

class SmsInDB(SmsBase):
    id: str
    status: SmsStatus
    created_at: datetime
    updated_at: Optional[datetime] = None
    error_message: Optional[str] = None

class SmsResponse(SmsInDB):
    pass

class SmsInboxResponse(BaseModel):
    items: List[SmsInDB]
    total: int