from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime
from enum import Enum
import sqlite3

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
    status: SmsStatus = SmsStatus.PENDING
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: Optional[datetime] = None
    error_message: Optional[str] = None
    user_id: Optional[str] = None  # Make sure this is included

class SmsResponse(SmsInDB):
    # Keep all fields from SmsInDB including user_id
    pass

class SmsInboxResponse(BaseModel):
    items: List[SmsInDB]
    total: int

class MessageInDB(BaseModel):
    id: str
    phone_number: str
    message: str
    status: SmsStatus
    direction: str
    user_id: str
    created_at: datetime
    updated_at: Optional[datetime] = None
    error_message: Optional[str] = None

# Check if the store_sms function properly saves the user_id
async def store_sms(self, sms: SmsInDB, direction: str = "outgoing", user_id: str = None) -> SmsInDB:
    # Make sure the function is inserting the user_id parameter into the database
    # e.g., in the SQL INSERT statement
    ...

def check_db_structure():
    conn = sqlite3.connect('./data/sms_gateway.db')
    cursor = conn.cursor()
    cursor.execute("PRAGMA table_info(messages)")
    columns = cursor.fetchall()
    conn.close()
    return [col[1] for col in columns]  # Returns column names

# Run this to check if user_id exists in your table
print(check_db_structure())