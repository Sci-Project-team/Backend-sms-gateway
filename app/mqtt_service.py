# app/services/mqtt_service.py
import paho.mqtt.client as mqtt
import threading
import logging
import json
import uuid
from datetime import datetime
from typing import Optional, Callable

logger = logging.getLogger(__name__)

class MQTTService:
    def __init__(self, broker="broker.emqx.io", port=1883, username="emqx", password="public"):
        self.client = mqtt.Client()
        self.client.username_pw_set(username, password)
        self.broker = broker
        self.port = port
        self.thread: Optional[threading.Thread] = None
        self.is_running = False
        self.storage_service = None
        self.message_handlers = {}

    def set_storage_service(self, storage_service):
        """Set storage service for database operations"""
        self.storage_service = storage_service

    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            logger.info("Connected to MQTT Broker!")
            # Subscribe to received messages topic
            client.subscribe("emqx/esp32/receivedmessages")
            logger.info("Subscribed to emqx/esp32/receivedmessages topic")
        else:
            logger.warning(f"Failed to connect, return code {rc}")

    def on_message(self, client, userdata, message):
        """Handle incoming MQTT messages from ESP32 devices"""
        try:
            topic = message.topic
            payload = message.payload.decode()
            logger.info(f"Received message on topic {topic}: {payload}")
            
            # Handle received SMS messages
            if topic == "emqx/esp32/receivedmessages":
                self._handle_received_sms(payload)
                
        except Exception as e:
            logger.error(f"Error processing MQTT message: {e}")

    def _handle_received_sms(self, payload):
        """Handle received SMS messages and store in database"""
        try:
            print(f"Handling received SMS payload: {payload}")
            # Parse the payload - expecting format: "From: +213782819451 | Message: Hello response"
            if payload.startswith("From: ") and " | Message: " in payload:
                phone_start = 6  # After "From: "
                phone_end = payload.find(" | Message: ")
                message_start = phone_end + 12  # After " | Message: "
                
                if phone_end != -1 and message_start < len(payload):
                    phone_number = payload[phone_start:phone_end].strip()
                    message_content = payload[message_start:].strip()
                    
                    # Store in database asynchronously
                    if self.storage_service:
                        import asyncio
                        import threading
                        
                        # Create a new thread to handle async database operation
                        def store_async():
                            loop = asyncio.new_event_loop()
                            asyncio.set_event_loop(loop)
                            try:
                                loop.run_until_complete(
                                    self._store_received_sms(phone_number, message_content)
                                )
                            finally:
                                loop.close()
                        
                        threading.Thread(target=store_async, daemon=True).start()
                    else:
                        logger.warning("Storage service not available for storing received SMS")
                else:
                    logger.warning(f"Invalid SMS format received: {payload}")
            else:
                logger.warning(f"Unexpected message format: {payload}")
                
        except Exception as e:
            logger.error(f"Error handling received SMS: {e}")

    async def _store_received_sms(self, phone_number: str, message_content: str):
        """Store received SMS in database"""
        try:
            from app.models.sms import SmsInDB, SmsStatus
            
            sms_id = str(uuid.uuid4())
            now = datetime.now()
            
            # Create SMS object for database storage
            received_sms = SmsInDB(
                id=sms_id,
                phone_number=phone_number,
                message=message_content,
                status=SmsStatus.RECEIVED,
                created_at=now,
                updated_at=now,
                error_message=None
            )
            
            # Store in database as incoming message
            await self.storage_service.store_sms(received_sms, direction="incoming")
            
            # Log the operation
            await self.storage_service.store_log(
                "INFO",
                "MQTT",
                f"Received SMS from {phone_number} stored in database",
                {"phone_number": phone_number, "message_id": sms_id}
            )
            
            logger.info(f"Received SMS from {phone_number} stored successfully with ID: {sms_id}")
            
        except Exception as e:
            logger.error(f"Failed to store received SMS: {e}")

    def start(self):
        if self.is_running:
            logger.warning("MQTT service is already running")
            return
            
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.is_running = True
        self.thread = threading.Thread(target=self._run, daemon=True)
        self.thread.start()
        logger.info("MQTT service thread started")

    def _run(self):
        try:
            self.client.connect(self.broker, self.port, keepalive=60)
            self.client.loop_forever()
        except Exception as e:
            logger.exception("MQTT connection failed: %s", str(e))
        finally:
            self.is_running = False

    def stop(self):
        if not self.is_running:
            logger.warning("MQTT service is not running")
            return
            
        self.is_running = False
        self.client.disconnect()
        if self.thread and self.thread.is_alive():
            self.thread.join(timeout=5)
        logger.info("MQTT client disconnected")

    def publish(self, topic: str, payload: str, qos: int = 0):
        """Publish a message to MQTT broker for ESP32 devices"""
        if self.is_running:
            self.client.publish(topic, payload, qos)
            logger.info(f"Published to {topic}: {payload}")
        else:
            logger.warning("Cannot publish: MQTT service is not running")
