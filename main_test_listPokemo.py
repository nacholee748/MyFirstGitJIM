
#-*- coding: utf-8 -*-

import requests

def get_pokemos(url = 'https://pokeapi.co/api/v2/pokemon-form',offset=0):
	args = {'offset':offset} if offset else {}

	response = requests.get(url)

	if response.status_code == 200:
		payload =  response.json()
		results = payload.get('results', [])

		if results:
			for pokemon in results:
				name = pokemon['name']
				print(name)

		next = raw_input("¿Continuar Listando [Y/N] ?").lower()

		if next == 'y':
			get_pokemos(offset = offset+20)
	

if __name__ == '__main__':
	url = 'https://pokeapi.co/api/v2/pokemon-form'
	get_pokemos()

	