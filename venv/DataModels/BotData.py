import json

class BotData:

	def __init__(self):
		with open('../configuration.txt') as json_file:
		    self.data = json.load(json_file)

	def get_bot_token(self) -> str:
		return self.data['token']

	def get_bot_admins(self) -> list:
		return self.data['bot_admins']


