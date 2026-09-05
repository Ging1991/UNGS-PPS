import requests

class Generador:

	def __init__(self, servidor):
		self.servidor = servidor
		self.temperature = 0.2
		self.num_ctx = 4000
		self.num_predict = 500

	def inferencia(self, contenido):

		payload = {
			"messages": [
				{
					"role": "user",
					"content": contenido
				}
			],
			"temperature": self.temperature,
			"max_tokens": self.num_predict
		}

		respuesta = requests.post(
			f"{self.servidor}/v1/chat/completions",
			json=payload,
			timeout=120
		)

		respuesta.raise_for_status()
		datos = respuesta.json()
		return datos["choices"][0]["message"]["content"]