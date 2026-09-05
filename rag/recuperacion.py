import numpy as np

class Recuperacion:

	def __init__(self, transformador, vector_bd, documento_bd, top_k):
		self.transformador = transformador
		self.vector_bd = vector_bd
		self.documento_bd = documento_bd
		self.top_k = top_k

	def buscar_coincidencias(self, texto):
		vectores = self.vector_bd.leer()
		documentos = self.documento_bd.leer()
		texto_vectorizado = np.array([self.transformador.procesar(texto)]).astype('float32')
		distancias, indices = vectores.search(texto_vectorizado, self.top_k)
		bloques_recuperados = []
			
		for indice in indices[0]:
			idx = int(indice)
			if 0 <= idx < len(documentos):
				bloques_recuperados.append(documentos[idx].replace("\n", " "))
		return bloques_recuperados