# app/services/gsm_service.py
import uuid
import logging
from datetime import datetime
from app.models.sms import SmsInDB, SmsStatus, SmsCreate
from app.services.storage import StorageService

logger = logging.getLogger(__name__)

class GSMService:
    def __init__(self, storage_service: StorageService):
        self.storage = storage_service
        logger.info("GSM service initialized (simulation mode)")
   
    async def send_sms(self, sms: SmsCreate) -> SmsInDB:
        """Simule l'envoi d'un SMS"""
        sms_id = str(uuid.uuid4())
        now = datetime.now()
       
        
        import random
        success = random.random() > 0.1

        sms_in_db = SmsInDB(
            id=sms_id,
            phone_number=sms.phone_number,
            message=sms.message,
            status=SmsStatus.SENT if success else SmsStatus.FAILED,
            created_at=now,
            updated_at=now,
            error_message=None if success else "Simulation d'échec d'envoi"
        )
       
        # Store in database
        await self.storage.store_sms(sms_in_db, direction="outgoing")
        await self.storage.store_log(
            "INFO" if success else "ERROR", 
            "GSM", 
            f"SMS {sms_id} {'sent' if success else 'failed'} to {sms.phone_number}",
            {"phone_number": sms.phone_number, "success": success}
        )
        
        return sms_in_db
   
    async def get_sent_messages(self):
        """Récupère tous les messages envoyés"""
        return await self.storage.get_sent_messages()
   
    async def get_inbox(self):
        """Récupère les messages reçus"""
        return await self.storage.get_inbox()

    # À utiliser pour les tests - simule la réception d'un message
    async def simulate_received_sms(self, phone_number: str, message: str):
        sms_id = str(uuid.uuid4())
        now = datetime.now()
       
        sms = SmsInDB(
            id=sms_id,
            phone_number=phone_number,
            message=message,
            status=SmsStatus.RECEIVED,
            created_at=now,
            updated_at=now
        )
       
        # Store in database
        await self.storage.store_sms(sms, direction="incoming")
        await self.storage.store_log(
            "INFO", 
            "GSM", 
            f"Received SMS from {phone_number}",
            {"phone_number": phone_number}
        )
        
        return sms