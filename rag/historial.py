class Historial:

	def __init__(self, json_bd, vector_bd, transformador):
		self.json_bd = json_bd
		self.vector_bd = vector_bd
		self.transformador = transformador

	def leer(self):
		return [str(item) for item in self.json_bd.leer()]

	def guardar(self, pregunta, respuesta):
		bloque = f"USUARIO: {pregunta}\nZEUS: {respuesta}"
		self.json_bd.guardar_acumulado([bloque])
		self.vector_bd.guardar_acumulado(self.transformador.procesar([bloque]))
