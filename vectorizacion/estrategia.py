class Estrategia:

	def __init__(self, longitud, solapamiento):
		self.longitud = longitud
		self.solapamiento = solapamiento

	def fragmentar(self, texto):
		bloques = []
		posicion = 0
		longitud_total = len(texto)
			
		while posicion < longitud_total:
			fin = posicion + self.longitud
			bloque = texto[posicion:fin]
			bloques.append(bloque)
			posicion += (self.longitud - self.solapamiento)
			
		return bloques