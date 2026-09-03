import json
import requests

DIRECCION_CONFIGURACION = "configuracion.json"

def inferencia(servidor, contenido):
	payload = {
		"messages": [
			{
				"role": "user",
				"content": contenido
			}
		]
	}

	respuesta = requests.post(
		f"{servidor}/v1/chat/completions",
		json=payload,
		timeout=120
	)

	respuesta.raise_for_status()
	datos = respuesta.json()
	return datos["choices"][0]["message"]["content"]

def prueba_de_humo(url_servicio):
	try:
		print(f"Intentando conectar al servidor LLM en: {url_servicio}...")
		respuesta = inferencia(url_servicio, "Responde únicamente con la palabra: OK")
		print(f"El servidor respondió: {respuesta.strip()}")
		print(f"Prueba existosa.")
		return True
	except requests.exceptions.ConnectionError:
		print("❌ Error de conexión: No se pudo conectar al servidor LLM.")
		return False
	except requests.exceptions.Timeout:
		print("❌ Error: El servidor tardó demasiado en responder (Timeout).")
		return False
	except Exception as e:
		print(f"❌ Error inesperado durante la prueba: {e}")
		return False

if __name__ == "__main__":
	with open(DIRECCION_CONFIGURACION, "r", encoding="utf-8") as archivo:
		configuracion = json.load(archivo)

	url_servicio = configuracion["url_servicio"]
	prueba_de_humo(url_servicio)