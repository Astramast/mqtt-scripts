import paho.mqtt.client as mqtt
import requests
import logging
import os

import settings


logger = logging.getLogger(__name__)


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
			requests.post(
			    settings.INCUBATOR_BASE_URL + '/space/change_status',
			    data={
			        'open': 1 if is_up else 0,
			        'secret': settings.INCUBATOR_SECRET,
			    }
			)


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
		client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
		client.on_connect = on_connect
		client.on_message = on_message

		client.connect(settings.MQTT_SERVER, MQTT_PORT, MQTT_KEEPALIVE)
		client.loop_forever()
	except Exception as e:
		logger.exception(f"Exception in MQTT listener, could not proceed, stopping. Error : {e}")
	print("terminé")

