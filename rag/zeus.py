import time
from almacenamiento.json_bd import JsonBD

class Zeus:

	def __init__(self, historial, generador, recuperacion_contexto, recuperacion_historial, aumentador, reescritura):
		self.historial = historial
		self.generador = generador
		self.recuperacion_contexto = recuperacion_contexto
		self.recuperacion_historial = recuperacion_historial
		self.aumentador = aumentador
		self.reescritura = reescritura

	def consultar(self, pregunta):
		inicio = time.time()
		
		print("PASO 1: Generar historial reciente.")
		historial_lista = self.historial.leer()[-4:]
		historial_lista.append(f"USUARIO: {pregunta}")
		historial_reciente = "\n".join(historial_lista)
		#print(historial_reciente)

		pregunta_autocontenida = self.reescritura.procesar(historial_reciente)
		print(f"PASO 2: Reescribir pregunta -> {pregunta_autocontenida}")

		print("PASO 3: Recupero el contexto")
		bloques = self.recuperacion_contexto.buscar_coincidencias(pregunta)

		contexto_actual = "\n\n- ".join(bloques)
		#print(contexto_actual)

		print("PASO 4: Calculo el historial lejano.")
		lista_lejano = self.recuperacion_historial.buscar_coincidencias(pregunta_autocontenida)
		historial_lejano = "\n".join(lista_lejano)
		#print(historial_lejano)

		print("PASO 5: Generar prompt final.")
		prompt_completo = self.aumentador.generar_prompt(contexto_actual, historial_reciente, historial_lejano, pregunta)
		#print(prompt_completo)

		tokens_estimados = len(prompt_completo) // 4
		print(f"PASO 6: Contar tokens a enviar -> {tokens_estimados}.")

		print("PASO 7: Generar respuesta.")
		respuesta = self.generador.inferencia(prompt_completo)

		print("PASO 8: Guardando resultados")
		self.historial.guardar(pregunta, respuesta)

		fin = time.time()
		tiempo_transcurrido = fin - inicio
		print(f"PASO 9: Calcular tiempo de respuesta: {tiempo_transcurrido:.2f} segundos.")
		
		return respuesta