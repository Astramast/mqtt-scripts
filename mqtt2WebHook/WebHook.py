import requests

class WebHook():
	def __init__(self, url):
		self.url = url
	
	def send(self, message):
		requests.post(self.url, json=message)

