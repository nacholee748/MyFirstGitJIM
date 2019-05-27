#-*- coding: utf-8 -*-

import requests

if __name__ == '__main__':
	client_id = '2c70d7efdc2155070210'
	client_secret = '3bafa4a9bc0fafeff46bbc5d8cd073d2cf14a81f'
	code = 'e4752b74607ccf144f9e'
	acces_token = '43f6ff2657416eb1b2cdcf17ec2c2ef7c02dfcf3'


	url = 'https://api.github.com/user/repos'
	payload = {'name': 'git_api_cf_comunidad'}
	headers = {'Accept': 'application/json', 'Authorization': 'token ' + acces_token}

	response = requests.post(url,headers=headers, json = payload)

	if response.status_code == 200:
		print(response.json())
	else:
		print(response.content)