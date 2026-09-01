import json
import subprocess
import time
import requests

URL = "http://127.0.0.1:8080"

def servidor_disponible():
	try:
		respuesta = requests.get(
			f"{URL}/v1/models",
			timeout=1
		)
		return respuesta.ok
	except requests.RequestException:
		return False

def iniciar_servidor(modelo):
	return subprocess.Popen([
		r"C:\Users\Carlos\Desktop\TESIS\LlamaVulcan\llama-server.exe",
		"-m", modelo,
		"-ngl", "999",
		"-c", "2048",
		"--host", "127.0.0.1",
		"--port", "8080"
	])

def esperar_servidor(proceso):
	while proceso.poll() is None:
		if servidor_disponible():
			return True

		time.sleep(0.5)
	return False

def main():
	if servidor_disponible():
		print("El servidor LLM ya estaba iniciado.")
		input("Presione ENTER para cerrar...")
		return
		
	with open("Datos/configuracion.json", "r", encoding="utf-8") as archivo:
		configuracion = json.load(archivo)

	modelo = configuracion["modelo_lenguaje"]

	print("Iniciando servidor LLM...")
	proceso = iniciar_servidor(modelo)

	if esperar_servidor(proceso):
		print("Servidor LLM listo.")
	else:
		print("No se pudo iniciar el servidor.")

if __name__ == "__main__":
	main()