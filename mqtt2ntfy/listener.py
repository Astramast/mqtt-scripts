import paho.mqtt.client as mqtt
import requests
import logging
import os

import settings


logger = logging.getLogger(__name__)

#Generic function to notify a server
def ntfy(server, topic, data, title, priority, tags, attach):
	requests.post(f"https://{server}/{topic}",
	data="{data}".encode(encoding="utf-8"),
	headers={
		"Title": f"{title}",
		"Priority": f"{priority}",
		"Tags": f"{tags}",
		"Attach": f"{attach}"
	})

def ntfySend(ntfyData, ntfyTitle, ntfyAttach):
	ntfy(NTFY_SERVER, NTFY_TOPIC, ntfyData, ntfyTitle, NTFY_PRIORITY, NTFY_TAGS, ntfyAttach)

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
	logger.info("Connected with result code " + str(rc))

	# Subscribing in on_connect() means that if we lose the connection and
	# reconnect then subscriptions will be renewed.
	client.subscribe(TOPIC)


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
	logger.info(msg.topic + " " + str(msg.payload))

	if msg.topic == TOPIC:
		try:
			assert msg.payload in (b"0", b"1")
		except AssertionError:
			logger.warning(f"Invalid message received in topic <{TOPIC}> : <{msg.payload}>")
		else:
			is_up = msg.payload == b"1"
			ntfyData = "Urlab is up" if is_up else "Urlab is down"
			ntfyTitle = "URLAB UP" if is_up else "URLAB DOWN"
			ntfyAttach = URL_IMAGE_UP if is_up else URL_IMAGE_DOWN
			ntfySend(ntfyData, ntfyTitle, ntfyAttach)

if __name__ == "__main__":
	logging.basicConfig(
		filename="{}/mqtt2http.log".format(os.path.dirname(os.path.abspath(__file__))),
		level=settings.LOG_LEVEL,
		filemode='a',
		format="%(levelname)s:%(name)s:[%(asctime)s] %(message)s",
		datefmt="%Y-%m-%d %H:%M:%S"
	)
	logging.getLogger("requests").setLevel(logging.WARNING)
	logging.getLogger("urllib3").setLevel(logging.WARNING)

	logging.info(" ")
	logging.info("-" * 20)
	logging.info(" ")

	try:
		client = mqtt.Client()
		client.on_connect = on_connect
		client.on_message = on_message

		client.connect(settings.MQTT_SERVER, 1883, 60)
		client.loop_forever()
	except Exception as e:
		logger.exception(f"Exception in MQTT listener, could not proceed, stopping. Error : {e}")

