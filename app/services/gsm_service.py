# app/services/gsm_service.py
# app/services/gsm_service.py
import uuid
import logging
import json
from datetime import datetime
from app.models.sms import SmsInDB, SmsStatus, SmsCreate
from app.services.storage import StorageService

logger = logging.getLogger(__name__)

class GSMService:
    def __init__(self, storage_service: StorageService, mqtt_service=None):
        self.storage = storage_service
        self.mqtt_service = mqtt_service
        logger.info("GSM service initialized (simulation mode)")
   
    async def send_sms(self, sms: SmsCreate) -> SmsInDB:
        """Publish phone number and message on MQTT topic emqx/esp32/sendmessage"""
        sms_id = str(uuid.uuid4())
        now = datetime.now()
        
        # Publish to MQTT topic with the specified format
        success = False
        error_message = None
        
        if self.mqtt_service and self.mqtt_service.is_running:
            try:
                # Format message as: "To: +213782819451 | Message: Hello from test"
                formatted_message = f"To: {sms.phone_number} | Message: {sms.message}"
                
                self.mqtt_service.publish("emqx/esp32/sendmessage", formatted_message)
                success = True
                logger.info(f"SMS published to MQTT topic: {formatted_message}")
            except Exception as e:
                error_message = f"MQTT publish failed: {str(e)}"
                logger.error(error_message)
        else:
            error_message = "MQTT service not available or not running"
            logger.warning(error_message)

        sms_in_db = SmsInDB(
            id=sms_id,
            phone_number=sms.phone_number,
            message=sms.message,
            status=SmsStatus.SENT if success else SmsStatus.FAILED,
            created_at=now,
            updated_at=now,
            error_message=error_message
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
   
    # ... rest of your methods remain the same

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
