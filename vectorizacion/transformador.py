import requests

class Transformador:

	def __init__(self, servidor):
		self.servidor = servidor

	def procesar(self, texto):

		payload = {
			"input": texto
		}

		respuesta = requests.post(
			f"{self.servidor}/v1/embeddings",
			json=payload,
			timeout=120
		)
		respuesta.raise_for_status()
		datos = respuesta.json()
		return datos["data"][0]["embedding"]