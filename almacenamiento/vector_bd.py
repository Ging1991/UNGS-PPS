import numpy as np
import os
import faiss

class VectorBD:

	def __init__(self, direccion):
		self.direccion = direccion

	def leer(self, dimension=768):
		if not os.path.exists(self.direccion):
			index = faiss.IndexFlatL2(dimension)
			faiss.write_index(index, self.direccion)
		return faiss.read_index(self.direccion)

	def guardar(self, vectores):
		dimension = vectores.shape[1]
		index = faiss.IndexFlatL2(dimension)
		index.add(vectores)
		faiss.write_index(index, self.direccion)

	def guardar_acumulado(self, vectores):
		vectores = np.array(vectores, dtype="float32")

		if vectores.ndim == 1:
			vectores = np.expand_dims(vectores, axis=0)
		index = self.leer()
		index.add(vectores)
		faiss.write_index(index, self.direccion)