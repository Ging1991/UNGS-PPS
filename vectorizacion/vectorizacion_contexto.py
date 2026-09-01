import numpy as np

class VectorizacionContexto:

	def __init__(self, transformador, lector_pdf, vector_bd, json_bd, estrategia):
		self.transformador = transformador
		self.lector_pdf = lector_pdf
		self.vector_bd = vector_bd
		self.json_bd = json_bd
		self.estrategia = estrategia

	def procesar(self):
		
		print("Paso 1: Extraer texto del PDF.")
		texto = self.lector_pdf.extraer_texto()

		print("Paso 2: Dividir el texto en bloques")
		bloques = self.estrategia.fragmentar(texto)

		print("Paso 3: Vectorizar los bloques.")
		vectores = self.vectorizar_bloques(bloques, False)

		print("Paso 4: Convertir los vectores en matriz.")
		matriz_vectores = np.array(vectores).astype('float32')
		
		print("Paso 5: Guardar los vectores y los documentos generados.")
		self.vector_bd.guardar(matriz_vectores)
		self.json_bd.guardar(bloques)

		print("Proceso finalizado correctamente.")

	def vectorizar_bloques(self, bloques, esPrueba=False):
		vectores = []
		for i, bloque in enumerate(bloques):
			vectores.append(self.transformador.procesar(bloque))
			if (i + 1) % 10 == 0 or (i + 1) == len(bloques):
				print(f"Procesados {i+1}/{len(bloques)} bloques.")
				if esPrueba:
					break

		return vectores