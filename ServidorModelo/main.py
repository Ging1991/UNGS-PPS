import json
import subprocess
import time
import requests

DIRECCION_CONFIGURACION = "configuracion.json"
# Conseguir el driver desde https://github.com/ggml-org/llama.cpp/releases

def esta_disponible(url_servicio):
	try:
		respuesta = requests.get(
			f"{url_servicio}/v1/models",
			timeout=1
		)
		return respuesta.ok
	except requests.RequestException:
		return False

def iniciar_servicio(driver, modelo, capas, contexto, servidor, puerto):
	return subprocess.Popen([
		driver,
		"-m", modelo,
		"-ngl", capas,
		"-c", contexto,
		"--host", servidor,
		"--port", puerto
	])

def esperar_proceso(proceso, url_servicio):
	while proceso.poll() is None:
		if esta_disponible(url_servicio):
			return True
		time.sleep(0.5)
	return False

def main():

	with open(DIRECCION_CONFIGURACION, "r", encoding="utf-8") as archivo:
		configuracion = json.load(archivo)

	url_servicio = configuracion["url_servicio"]
	driver = configuracion["driver"]
	modelo = configuracion["modelo"]
	capas = configuracion["capas"]
	contexto = configuracion["contexto"]
	servidor = configuracion["servidor"]
	puerto = configuracion["puerto"]

	if esta_disponible(url_servicio):
		print("El servidor LLM ya estaba iniciado.")
		print("Puede cerrar esta ventana sin problemas.")
		input("Presione ENTER para continuar...")
		return
		
	print("Iniciando servidor LLM...")
	proceso = iniciar_servicio(driver, modelo, capas, contexto, servidor, puerto)

	if esperar_proceso(proceso, url_servicio):
		print("Servidor LLM listo.")
		print("No cierre esta ventana mientras utiliza el sistema IA.")
	else:
		print("No se pudo iniciar el servidor.")

if __name__ == "__main__":
	main()