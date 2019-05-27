#-*- coding: utf-8 -*-

import requests

client_id = '2c70d7efdc2155070210'
client_secret = '3bafa4a9bc0fafeff46bbc5d8cd073d2cf14a81f'
code = '64962846de39c1d40918'

if __name__ == '__main__':

	url = 'https://api.github.com/user/repos'
	headers = {'Authorization': 'token 91bc2d2e2af23ec8f87a3fa28983dda5fddb4343'}

	response = requests.get(url,headers=headers)

	if response.status_code == 200:
		payload = response.json()

		for project in payload:
			name = project['name']
			print(name)
	else:
		print(response.content)
