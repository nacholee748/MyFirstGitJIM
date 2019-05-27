import requests
import json

# POST para crear Recursos
if __name__ == '__main__':
	url = 'http://httpbin.org/post'
	payload = {'nombre':'eduardo','curso':'python','nivel':'intermedio'}

	headers = {'content-Type':'application/json','access-token':'12345'}

	response = requests.post(url,json=payload,headers=headers)
	#json post se encarga de serializarlo -> json=payload
	#data entoncs nosotros lo debemos serializar, de lo contrario queda cargado solo en el atributo form -> data=json.dumps(payload)
	print(response.url) 

	if response.status_code == 200:
		headers_response = response.headers # Dic
		# print(headers_response)
		server = headers_response['Server']
		print(server)
		# print(response.content)