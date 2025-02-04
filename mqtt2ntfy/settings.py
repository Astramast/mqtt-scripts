import os
import logging


MQTT_SERVER = os.environ.get("MQTT_HOST", "localhost")

INCUBATOR_BASE_URL = "https://urlab.be"
INCUBATOR_SECRET = os.environ.get("INCUBATOR_SECRET", "vairie secrette")
LOG_LEVEL = logging.DEBUG
TOPIC = os.environ.get("TOPIC", "opinator")

NTFY_SERVER = os.environ.get("NTFY_SERVER", "https://example.org/ntfy")
NTFY_TOPIC = os.environ.get("NTFY_TOPIC", "UrLab")
NTFY_PRIORITY = os.environ.get("NTFY_PRIORITY", "urgent")
NTFY_TAGS = os.environ.get("NTFY_TAGS", "no_entry")
URL_IMAGE_UP = os.environ.get("URL_IMAGE_UP", "https://urlab.be/static/img/space-invaders-open.png")
URL_IMAGE_DOWN = os.environ.get("URL_IMAGE_DOWN", "https://urlab.be/static/img/space-invaders-closed.png")

