import uuid
import logging
from datetime import datetime
from app.models.sms import SmsInDB, SmsStatus, SmsCreate

logger = logging.getLogger(__name__)

# Version simulation - À remplacer par la vraie communication série plus tard
class GSMService:
    def __init__(self):
        self.sent_messages = {}
        self.received_messages = []
        logger.info("GSM service initialized (simulation mode)")
    
    async def send_sms(self, sms: SmsCreate) -> SmsInDB:
        """Simule l'envoi d'un SMS"""
        sms_id = str(uuid.uuid4())
        now = datetime.now()
        
        # En simulation, 90% des SMS sont envoyés avec succès
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
        
        self.sent_messages[sms_id] = sms_in_db
        logger.info(f"SMS {sms_id} {'sent' if success else 'failed'} to {sms.phone_number}")
        return sms_in_db
    
    async def get_sent_messages(self):
        """Récupère tous les messages envoyés"""
        return list(self.sent_messages.values())
    
    async def get_inbox(self):
        """Récupère les messages reçus"""
        return self.received_messages

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
        
        self.received_messages.append(sms)
        logger.info(f"Received SMS from {phone_number}")
        return sms