import requests

# GET para Obtener Recursos
if __name__ == '__main__':
	url = 'https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/deadpool-vengadores-infinity-war-1540739153.jpg?resize=768:*'
	args = {'nombre':'eduardo','curso':'python','nivel':'intermedio'}
	response = requests.get(url, stream = True) #stream se usa para dejar la conexion abierta cuando son archivos pesados
	with  open('imagen.jpg', 'wb') as file:
		for chunk in response.iter_content(): # Este ciclo toma todo el contenido del server y la descarga poco a poco, es importante para archivos pesados
			file.write(chunk)

	response.close #cerramos la conexion
	