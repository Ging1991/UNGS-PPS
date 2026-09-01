def crear_promp(pregunta, contexto):
	return f"""

[ROL]
- Eres un juez estricto de recuperación de información (RAG).

[INSTRUCCIÓN]
- Evalúa rigurosamente el contexto frente a la pregunta bajo estos 4 criterios.
- Para cada criterio selecciona una categoria.

Criterio 1: ¿El contexto contiene información necesaria para responder a la pregunta?
SUFICIENTE: El contexto contiene toda la información necesaria para responder la pregunta.
INSUFICIENTE: El contexto NO contiene la información necesaria para responder la pregunta.

Criterio 2. Tipo de relación del contexto con la pregunta
RELACIONADO: Habla de algo RELACIONADO a lo que se pregunta.
NO_RELACIONADO: Habla de un tema NO RELACIONADO a lo que se pregunta.

Criterio 3. Nivel de ruido:
SIN_RUIDO: Contiene la informacion justa y necesaria
CON_RUIDO: Contiene información extra no necesaria, o irrelevante.

Criterio 4. Utilidad del contexto:
UTIL: Puedo contestar la pregunta con ese contexto.
INUTIL: No puedo contestar la pregunta con ese contexto.

REGLA ESTRICTA DE SALIDA:
- Devuelve ÚNICAMENTE las 4 palabras seleccionadas en una sola línea separadas por un espacio.
- No incluyas explicaciones, viñetas ni texto adicional.

[PREGUNTA] {pregunta}
[CONTEXTO] {contexto}

Respuesta:"""

def prompt_relacion_min(pregunta, contexto):
	return crear_prompt_binario(pregunta, contexto, "¿el contexto proporcionado se encuentra minimamente relacionado a la pregunta del usuario?")

def prompt_relacion_max(pregunta, contexto):
	return crear_prompt_binario(pregunta, contexto, "¿el contexto proporcionado se encuentra estrechamente relacionado a la pregunta del usuario?")

def prompt_ruido(pregunta, contexto):
	return crear_prompt_binario(pregunta, contexto, "¿el contexto proporcionado tiene mas infomración de la necesaria para responder a la pregunta del usuario?")


def crear_prompt_binario(pregunta, contexto, pregunta_binaria):
	return f"""
Analiza el contexto y responde a esta única pregunta: {pregunta_binaria}
Responde ÚNICAMENTE con la palabra "SI" o la palabra "NO". No des explicaciones.

PREGUNTA: {pregunta}
CONTEXTO: {contexto}

RESPUESTA (SI/NO):
"""

def crear_prompt_vf(pregunta, contexto, afirmacion):
	return f"""
- Eres un analista de información confiable y estricto.
- Analiza la afirmación que trata sobre el contexto y la pregunta.
- Decide si la afirmación es verdadera o falsa.
VERDADERO: La afirmación sobre el contexto y la pregunta es verdadera y correcta.
FALSO:La afirmación sobre el contexto y la pregunta es falsa o incorrecta.
- Responde ÚNICAMENTE con la palabra "VERDADERO" o la palabra "FALSO".
- No des explicaciones ni escribas nada mas.

AFIRMACIÓN: {afirmacion}
PREGUNTA: {pregunta}
CONTEXTO: {contexto}

RESPUESTA (VERDADERO/FALSO):
"""