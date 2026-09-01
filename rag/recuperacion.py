import re
import numpy as np

class Recuperacion:

	def __init__(self, transformador, vector_bd, documento_bd, top_k):
		self.transformador = transformador
		self.vector_bd = vector_bd
		self.documento_bd = documento_bd
		self.top_k = top_k

	def buscar_coincidencias(self, texto, tipo):
		vectores = self.vector_bd.leer()
		documentos = self.documento_bd.leer()
		texto_vectorizado = np.array([self.transformador.procesar(texto)]).astype('float32')
		distancias, indices = vectores.search(texto_vectorizado, self.top_k)
		bloques_recuperados = []
			
		for indice in indices[0]:
			idx = int(indice)
			if 0 <= idx < len(documentos):
				bloques_recuperados.append(documentos[idx].replace("\n", " "))
		if (tipo == 1):
			return bloques_recuperados
		if (tipo == 2):
			return self.reranking_exacto(bloques_recuperados, texto)
		if (tipo == 3):
			return self.reranking_mejor_relleno([], bloques_recuperados, texto)
		return None

	def reranking_exacto(self, fragmentos, pregunta):
		fragmentos_con_puntaje = []
		for fragmento in fragmentos:
			score = self.puntaje_exacto(fragmento, pregunta)
			fragmentos_con_puntaje.append((fragmento, score))

		fragmentos_con_puntaje.sort(key=lambda x: x[1], reverse=True)
		fragmentos_ordenados = [fragmento for fragmento, score in fragmentos_con_puntaje]
		return fragmentos_ordenados

	def reranking_mejor_relleno(self, fragmentos_actuales, fragmentos_restantes, pregunta):
		if len(fragmentos_restantes) == 0:
			return fragmentos_actuales

		if len(fragmentos_actuales) == 0:
			nuevos_actuales = [fragmentos_restantes[0]]
			nuevos_restantes = fragmentos_restantes[1:]
			return self.reranking_mejor_relleno(nuevos_actuales, nuevos_restantes, pregunta)

		acumulado = "-".join(fragmentos_actuales)

		fragmentos_con_puntaje = []
		for fragmento in fragmentos_restantes:
			score = self.puntaje_exacto(fragmento + acumulado, pregunta)
			fragmentos_con_puntaje.append((fragmento, score))

		fragmentos_con_puntaje.sort(key=lambda x: x[1], reverse=True)
		mejor_fragmento = fragmentos_con_puntaje[0][0]
		nuevos_actuales = list(fragmentos_actuales) + [mejor_fragmento]
		nuevos_restantes = [f for f in fragmentos_restantes if f != mejor_fragmento]
		return self.reranking_mejor_relleno(nuevos_actuales, nuevos_restantes, pregunta)

	def limpiar_texto(self, texto):
		texto = texto.lower()
		texto = texto.encode('ascii', 'ignore').decode('ascii')
		texto_limpio = re.sub(r'[^a-z0-9\s]', ' ', texto)
		return texto_limpio

	def puntaje_exacto(self, fragmento, pregunta):
		pregunta_limpia = self.limpiar_texto(pregunta)
		fragmento_limpio = self.limpiar_texto(fragmento)
		palabras_pregunta = set(pregunta_limpia.split())
		palabras_fragmento = set(fragmento_limpio.split())
		contador = 0
		for palabra in palabras_fragmento:
			if palabra in palabras_pregunta:
				contador += 1

		return contador
