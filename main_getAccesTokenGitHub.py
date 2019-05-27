#-*- coding: utf-8 -*-

import requests

client_id = '2c70d7efdc2155070210'
client_secret = '3bafa4a9bc0fafeff46bbc5d8cd073d2cf14a81f'
code = 'e4752b74607ccf144f9e'

if __name__ == '__main__':

	url = 'https://github.com/login/oauth/access_token'
	payload = {'client_id':client_id,'client_secret':client_secret,'code':code}
	headers = {'Accept': 'application/json'}

	response = requests.post(url,json=payload,headers=headers)

	if response.status_code == 200:
		response_json = response.json()

		access_token = response_json['access_token']
		#access_token = '91bc2d2e2af23ec8f87a3fa28983dda5fddb4343'
		print(access_token)
