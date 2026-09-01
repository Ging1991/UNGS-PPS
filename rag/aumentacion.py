class Aumentacion:

	def __init__(self, direccion):
		self.direccion = direccion

	def generar_prompt(self, contexto, historial_reciente, historial_lejano, pregunta):
		with open(self.direccion, "r", encoding="utf-8") as archivo:
			texto = archivo.read()

		texto = texto.replace("[CONTEXTO]", contexto)
		texto = texto.replace("[HISTORIAL_RECIENTE]", historial_reciente)
		texto = texto.replace("[HISTORIAL_LEJANO]", historial_lejano)
		texto = texto.replace("[PREGUNTA]", pregunta)

		return texto

