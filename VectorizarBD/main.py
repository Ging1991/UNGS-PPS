import sys
from pathlib import Path

raiz_proyecto = Path(__file__).resolve().parent.parent
sys.path.append(str(raiz_proyecto))

from vectorizacion.vectorizacion_contexto import VectorizacionContexto
from vectorizacion.transformador import Transformador
from vectorizacion.estrategia import Estrategia
from almacenamiento.lector_pdf import LectorPDF
from almacenamiento.vector_bd import VectorBD
from almacenamiento.json_bd import JsonBD
import json

DIRECCION_CONFIGURACION = "configuracion.json"

def VectorizarBD():
	print("****************** PROCESO DE VECTORIZACIÓN DE L BASE DE DATOS ******************")
	with open(DIRECCION_CONFIGURACION, "r", encoding="utf-8") as archivo:
		configuracion = json.load(archivo)

	transformador = Transformador(configuracion["url_servicio"])
	lector_pdf = LectorPDF(configuracion["direccionPDF"])
	vector_bd = VectorBD(configuracion["direccionVectores"])
	json_bd = JsonBD(configuracion["direccionJSON"])
	estrategia = Estrategia(500, 100)
	vectorizador_contexto = VectorizacionContexto(transformador, lector_pdf, vector_bd, json_bd, estrategia)
	vectorizador_contexto.procesar()

if __name__ == "__main__":
	VectorizarBD()