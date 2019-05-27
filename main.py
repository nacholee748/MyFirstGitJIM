#-*- coding: utf-8 -*-

import requests

if __name__ == '__main__':
	url = 'https://api.github.com/user'

	session = requests.session()
	session.auth = ('nacholee748@gmail.com','J.Nacho09')

	response = session.get(url)

	if response.ok:
		response = session.get('https://github.com/nacholee748/')

		if response.ok:
			print(response.cookies)
		else:
			print(response.content)