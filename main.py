from rag.historial import Historial
from rag.generador import Generador
from rag.recuperacion import Recuperacion
from vectorizacion.transformador import Transformador
from rag.zeus import Zeus
from almacenamiento.json_bd import JsonBD
from almacenamiento.vector_bd import VectorBD
from rag.chat import Chat
from rag.aumentacion import Aumentacion
from servicios.reescritura import Reescritura

DIRECCION_PLANTILLA_PROMPT_PRINCIPAL = "datos/plantilla_instruccion.txt"
DIRECCION_PLANTILLA_PROMPT_REESCRITURA = "datos/plantilla_reescritura.txt"
DIRECCION_VECTOR_CONTEXTO = "datos/index.faiss"
DIRECCION_JSON_CONTEXTO = "datos/documentos.json"
DIRECCION_VECTOR_HISTORIAL = "datos/historial.faiss"
DIRECCION_JSON_HISTORIAL = "datos/historial.json"
URL_TRANSFORMADOR = "http://127.0.0.1:8081"
URL_GENERADOR = "http://127.0.0.1:8080"
TOP_K = 5

if __name__ == "__main__":
	historial_json_bd = JsonBD(DIRECCION_JSON_HISTORIAL)
	historial_vector_bd = VectorBD(DIRECCION_VECTOR_HISTORIAL)
	contexto_json_bd = JsonBD(DIRECCION_JSON_CONTEXTO)
	contexto_vector_bd = VectorBD(DIRECCION_VECTOR_CONTEXTO)

	transformador = Transformador(URL_TRANSFORMADOR)
	historial = Historial(historial_json_bd, historial_vector_bd, transformador)
	recuperacion = Recuperacion(transformador, contexto_vector_bd, contexto_json_bd, TOP_K)
	recuperacion_h = Recuperacion(transformador, historial_vector_bd, historial_json_bd, TOP_K)
	generador = Generador(URL_GENERADOR)
	aumentacion = Aumentacion(DIRECCION_PLANTILLA_PROMPT_PRINCIPAL)
	reescritura = Reescritura(DIRECCION_PLANTILLA_PROMPT_REESCRITURA, generador)
	zeus = Zeus(historial, generador, recuperacion, recuperacion_h, aumentacion, reescritura)
	chat = Chat(zeus)
	chat.comenzar()