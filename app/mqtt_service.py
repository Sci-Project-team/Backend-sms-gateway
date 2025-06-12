# app/services/mqtt_service.py
import paho.mqtt.client as mqtt
import threading
import logging
import asyncio
from typing import Optional

logger = logging.getLogger(__name__)

class MQTTService:
    def __init__(self, broker="broker.emqx.io", port=1883, username="emqx", password="public"):
        self.client = mqtt.Client()
        self.client.username_pw_set(username, password)
        self.broker = broker
        self.port = port
        self.thread: Optional[threading.Thread] = None
        self.is_running = False

    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            logger.info("Connected to MQTT Broker!")
            # Subscribe to topics here if needed
            # client.subscribe("your/topic")
        else:
            logger.warning(f"Failed to connect, return code {rc}")

    def on_message(self, client, userdata, message):
        """Handle incoming MQTT messages"""
        try:
            topic = message.topic
            payload = message.payload.decode()
            logger.info(f"Received message on topic {topic}: {payload}")
            # Process your MQTT messages here
        except Exception as e:
            logger.error(f"Error processing MQTT message: {e}")

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
        """Publish a message to MQTT broker"""
        if self.is_running:
            self.client.publish(topic, payload, qos)
            logger.info(f"Published to {topic}: {payload}")
        else:
            logger.warning("Cannot publish: MQTT service is not running")
