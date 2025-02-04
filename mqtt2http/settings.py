import os
import logging


MQTT_SERVER = os.environ.get("MQTT_HOST", "localhost")

INCUBATOR_BASE_URL = "https://urlab.be"
INCUBATOR_SECRET = os.environ.get("INCUBATOR_SECRET", "vairie secrette")
LOG_LEVEL = logging.DEBUG
TOPIC = os.environ.get("TOPIC", "opinator")

