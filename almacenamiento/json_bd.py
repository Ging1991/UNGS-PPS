import os
import json

class JsonBD:

	def __init__(self, direccion):
		self.direccion = direccion

	def leer(self):
		if not os.path.exists(self.direccion):
			self.guardar([])
			return []

		with open(self.direccion, "r", encoding="utf-8") as archivo:
			datos = json.load(archivo)

		return datos

	def guardar(self, datos):
		with open(self.direccion, "w", encoding="utf-8") as archivo:
			json.dump(datos, archivo, ensure_ascii=False, indent=2)

	def guardar_acumulado(self, bloques):
		print("guardar acum json")
		documentos = self.leer()
		documentos.extend(bloques)
		self.guardar(documentos)