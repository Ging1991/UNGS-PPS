from vectorizacion.vectorizacion_contexto import VectorizacionContexto
from vectorizacion.transformador import Transformador
from vectorizacion.estrategia import Estrategia
from almacenamiento.lector_pdf import LectorPDF
from almacenamiento.vector_bd import VectorBD
from almacenamiento.json_bd import JsonBD

DIRECCION_PDF = "datos/guion.pdf"
DIRECCION_VECTORES = "datos/index.faiss"
DIRECCION_JSON = "datos/documentos.json"
URL_PROCESO_VECTORIZACION = "http://127.0.0.1:8081"

if __name__ == "__main__":
	print("****************** PROCESO DE VECTORIZACIÓN ******************")
	transformador = Transformador(URL_PROCESO_VECTORIZACION)
	lector_pdf = LectorPDF(DIRECCION_PDF)
	vector_bd = VectorBD(DIRECCION_VECTORES)
	json_bd = JsonBD(DIRECCION_JSON)
	estrategia = Estrategia(500, 100)
	vectorizador_contexto = VectorizacionContexto(transformador, lector_pdf, vector_bd, json_bd, estrategia)
	vectorizador_contexto.procesar()