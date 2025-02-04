import os
import logging


MQTT_SERVER = os.environ.get("MQTT_HOST", "localhost")

INCUBATOR_BASE_URL = "https://urlab.be"
INCUBATOR_SECRET = os.environ.get("INCUBATOR_SECRET", "vairie secrette")
LOG_LEVEL = logging.DEBUG
TOPIC = os.environ.get("TOPIC", "opinator")
MQTT_PORT = os.environ.get("MQTT_PORT", 1883)
MQTT_KEEPALIVE = os.environ.get("MQTT_KEEPALIVE", 60)

