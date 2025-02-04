import os
import logging


MQTT_SERVER = os.environ.get("MQTT_HOST", "localhost")

INCUBATOR_BASE_URL = "https://urlab.be"
INCUBATOR_SECRET = os.environ.get("INCUBATOR_SECRET", "vairie secrette")
LOG_LEVEL = logging.DEBUG
TOPIC = os.environ.get("TOPIC", "opinator")
MQTT_PORT = os.environ.get("MQTT_PORT", 1883)
MQTT_KEEPALIVE = os.environ.get("MQTT_KEEPALIVE", 60)

WEBHOOK_URL = os.environ.get("WEBHOOK_URL", "http://localhost:5000/webhook")
WEBHOOK_UP_FILE = os.environ.get("WEBHOOK_UP_FILE", "urlab-is-open.json")
WEBHOOK_DOWN_FILE = os.environ.get("WEBHOOK_DOWN_FILE", "urlab-is-closed.json")

