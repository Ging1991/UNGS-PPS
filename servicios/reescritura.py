class Reescritura:

	def __init__(self, direccion, generador):
		self.direccion = direccion
		self.generador = generador

	def procesar(self, historial):
		with open(self.direccion, "r", encoding="utf-8") as archivo:
			texto = archivo.read()

		texto = texto.replace("[HISTORIAL]", historial)
		texto = self.generador.inferencia(texto)
		return texto