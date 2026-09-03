import json
import requests
import os

os.system('')

DIRECCION_CONFIGURACION = "configuracion.json"

def obtener_embedding(servidor, texto):
	payload = {
		"input": texto
	}

	respuesta = requests.post(
		f"{servidor}/v1/embeddings",
		json=payload,
		timeout=120
	)

	respuesta.raise_for_status()
	datos = respuesta.json()
	return datos["data"][0]["embedding"]

def prueba_de_humo(url_servicio):
	try:
		print(f"Intentando conectar al servidor de embeddings en: {url_servicio}...")
		vector = obtener_embedding(url_servicio, "Prueba de humo para embeddings")
		
		if isinstance(vector, list) and len(vector) > 0:
			print(f"\033[32mPrueba exitosa: \033[0mSe generó un vector con una dimensión de {len(vector)} valores.")
			print(f"Primeros valores del vector: {vector[:3]}...")
			return True
		else:
			print("❌ Error: El servidor respondió pero el formato del vector no es válido.")
			return False

	except requests.exceptions.ConnectionError:
		print("❌ Error de conexión: No se pudo conectar al servidor de vectorización.")
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

	prueba_de_humo(configuracion["url_servicio"])