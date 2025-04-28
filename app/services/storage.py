# app/services/storage.py
import sqlite3
import aiosqlite
from pathlib import Path
import logging
import json
from datetime import datetime
from typing import List, Optional, Dict, Any
import uuid


from app.models.sms import SmsInDB, SmsCreate, SmsStatus
from app.models.user import UserInDB, UserCreate

logger = logging.getLogger(__name__)

DATABASE_PATH = Path("./data/sms_gateway.db")
DATABASE_PATH.parent.mkdir(exist_ok=True)

class StorageService:
    def __init__(self):
        self._create_tables_if_not_exist()
        logger.info(f"Storage service initialized with SQLite at {DATABASE_PATH}")
    
    def _create_tables_if_not_exist(self):
        conn = sqlite3.connect(str(DATABASE_PATH))
        cursor = conn.cursor()
        
        # Create users table
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id TEXT PRIMARY KEY,
            username TEXT UNIQUE NOT NULL,
            email TEXT UNIQUE NOT NULL,
            full_name TEXT,
            hashed_password TEXT NOT NULL,
            api_key TEXT UNIQUE NOT NULL,
            created_at TEXT NOT NULL,
            is_active INTEGER NOT NULL
        )
        ''')
        
        # Create messages table
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS messages (
            id TEXT PRIMARY KEY,
            phone_number TEXT NOT NULL,
            message TEXT NOT NULL,
            status TEXT NOT NULL,
            created_at TEXT NOT NULL,
            updated_at TEXT,
            error_message TEXT,
            direction TEXT NOT NULL
        )
        ''')
        
        # Create logs table
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS logs (
            id TEXT PRIMARY KEY,
            timestamp TEXT NOT NULL,
            level TEXT NOT NULL,
            component TEXT NOT NULL,
            message TEXT NOT NULL,
            metadata TEXT
        )
        ''')
        
        conn.commit()
        conn.close()
    
    async def create_user(self, user: UserCreate, hashed_password: str, api_key: str) -> UserInDB:
        async with aiosqlite.connect(str(DATABASE_PATH)) as db:
            user_id = str(uuid.uuid4())
            now = datetime.now().isoformat()
            
            await db.execute(
                '''
                INSERT INTO users (id, username, email, full_name, hashed_password, api_key, created_at, is_active)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                ''',
                (user_id, user.username, user.email, user.full_name, 
                 hashed_password, api_key, now, True)
            )
            await db.commit()
            
            return UserInDB(
                id=user_id,
                username=user.username,
                email=user.email,
                full_name=user.full_name,
                hashed_password=hashed_password,
                api_key=api_key,
                created_at=datetime.fromisoformat(now),
                is_active=True
            )
    
    async def get_user_by_api_key(self, api_key: str) -> Optional[UserInDB]:
        async with aiosqlite.connect(str(DATABASE_PATH)) as db:
            async with db.execute(
                'SELECT * FROM users WHERE api_key = ?',
                (api_key,)
            ) as cursor:
                user = await cursor.fetchone()
                
                if not user:
                    return None
                    
                columns = [description[0] for description in cursor.description]
                user_dict = dict(zip(columns, user))
                
                return UserInDB(
                    id=user_dict['id'],
                    username=user_dict['username'],
                    email=user_dict['email'],
                    full_name=user_dict['full_name'],
                    hashed_password=user_dict['hashed_password'],
                    api_key=user_dict['api_key'],
                    created_at=datetime.fromisoformat(user_dict['created_at']),
                    is_active=bool(user_dict['is_active'])
                )
    
    async def store_sms(self, sms: SmsInDB, direction: str = "outgoing") -> SmsInDB:
        async with aiosqlite.connect(str(DATABASE_PATH)) as db:
            await db.execute(
                '''
                INSERT INTO messages (id, phone_number, message, status, created_at, updated_at, error_message, direction)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                ''',
                (sms.id, sms.phone_number, sms.message, sms.status.value, 
                 sms.created_at.isoformat(), 
                 sms.updated_at.isoformat() if sms.updated_at else None,
                 sms.error_message, direction)
            )
            await db.commit()
            return sms
    
    async def get_sent_messages(self) -> List[SmsInDB]:
        async with aiosqlite.connect(str(DATABASE_PATH)) as db:
            async with db.execute(
                'SELECT * FROM messages WHERE direction = "outgoing" ORDER BY created_at DESC'
            ) as cursor:
                messages = await cursor.fetchall()
                columns = [description[0] for description in cursor.description]
                
                result = []
                for message in messages:
                    msg_dict = dict(zip(columns, message))
                    result.append(SmsInDB(
                        id=msg_dict['id'],
                        phone_number=msg_dict['phone_number'],
                        message=msg_dict['message'],
                        status=SmsStatus(msg_dict['status']),
                        created_at=datetime.fromisoformat(msg_dict['created_at']),
                        updated_at=datetime.fromisoformat(msg_dict['updated_at']) if msg_dict['updated_at'] else None,
                        error_message=msg_dict['error_message']
                    ))
                return result
    
    async def get_inbox(self) -> List[SmsInDB]:
        async with aiosqlite.connect(str(DATABASE_PATH)) as db:
            async with db.execute(
                'SELECT * FROM messages WHERE direction = "incoming" ORDER BY created_at DESC'
            ) as cursor:
                messages = await cursor.fetchall()
                columns = [description[0] for description in cursor.description]
                
                result = []
                for message in messages:
                    msg_dict = dict(zip(columns, message))
                    result.append(SmsInDB(
                        id=msg_dict['id'],
                        phone_number=msg_dict['phone_number'],
                        message=msg_dict['message'],
                        status=SmsStatus(msg_dict['status']),
                        created_at=datetime.fromisoformat(msg_dict['created_at']),
                        updated_at=datetime.fromisoformat(msg_dict['updated_at']) if msg_dict['updated_at'] else None,
                        error_message=msg_dict['error_message']
                    ))
                return result
    
    async def store_log(self, level: str, component: str, message: str, metadata: Dict[str, Any] = None) -> str:
        async with aiosqlite.connect(str(DATABASE_PATH)) as db:
            log_id = str(uuid.uuid4())
            now = datetime.now().isoformat()
            
            await db.execute(
                '''
                INSERT INTO logs (id, timestamp, level, component, message, metadata)
                VALUES (?, ?, ?, ?, ?, ?)
                ''',
                (log_id, now, level, component, message, json.dumps(metadata) if metadata else None)
            )
            await db.commit()
            return log_id
    
    async def get_logs(self, limit: int = 100) -> List[Dict[str, Any]]:
        async with aiosqlite.connect(str(DATABASE_PATH)) as db:
            async with db.execute(
                'SELECT * FROM logs ORDER BY timestamp DESC LIMIT ?',
                (limit,)
            ) as cursor:
                logs = await cursor.fetchall()
                columns = [description[0] for description in cursor.description]
                
                result = []
                for log in logs:
                    log_dict = dict(zip(columns, log))
                    log_dict['metadata'] = json.loads(log_dict['metadata']) if log_dict['metadata'] else None
                    result.append(log_dict)
                return result

    async def get_user_by_username(self, username: str) -> Optional[UserInDB]:
        async with aiosqlite.connect(str(DATABASE_PATH)) as db:
            async with db.execute(
                 'SELECT * FROM users WHERE username = ?',
                (username,)
            ) as cursor:
                user = await cursor.fetchone()
            
                if not user:
                    return None
                
                columns = [description[0] for description in cursor.description]
                user_dict = dict(zip(columns, user))
            
                return UserInDB(
                    id=user_dict['id'],
                    username=user_dict['username'],
                    email=user_dict['email'],
                    full_name=user_dict['full_name'],
                    hashed_password=user_dict['hashed_password'],
                    api_key=user_dict['api_key'],
                    created_at=datetime.fromisoformat(user_dict['created_at']),
                    is_active=bool(user_dict['is_active'])
                )

    async def get_all_users(self) -> List[Dict[str, Any]]:
        async with aiosqlite.connect(str(DATABASE_PATH)) as db:
            async with db.execute('SELECT * FROM users') as cursor:
                users = await cursor.fetchall()
                columns = [description[0] for description in cursor.description]
            
                result = []
                for user in users:
                    user_dict = dict(zip(columns, user))
                    user_dict.pop('hashed_password', None)
                    result.append(user_dict)
                return result

    async def get_all_messages(self) -> List[Dict[str, Any]]:
        async with aiosqlite.connect(str(DATABASE_PATH)) as db:
            async with db.execute('SELECT * FROM messages ORDER BY created_at DESC') as cursor:
                messages = await cursor.fetchall()
                columns = [description[0] for description in cursor.description]
            
                result = []
                for message in messages:
                    msg_dict = dict(zip(columns, message))
                    result.append(msg_dict)
                return result