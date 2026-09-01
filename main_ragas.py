import os
from rag.generador import Generador
from ragas.generador import crear_prompt_binario
from ragas.generador import crear_prompt_vf

DIRECCION_RES_MEJOR_RELLENO = "Datos\\mejor_relleno_resultados.json"
URL_GENERADOR = "http://127.0.0.1:8080"

def resultado(respuesta):
	texto_limpio = respuesta.strip().upper()

	if "SI" in texto_limpio:
		print("\033[32mSI\033[0m")
	elif "NO" in texto_limpio:
		print("\033[31mNO\033[0m")
	else:
		print(f"\033[34mDESCONOCIDO ({respuesta.strip()})\033[0m")

def resultado_vf(respuesta):
	texto_limpio = respuesta.strip().upper()

	if "VERDADERO" in texto_limpio:
		return "\033[32mVERDADERO\033[0m"
	elif "FALSO" in texto_limpio:
		return "\033[31mFALSO\033[0m"
	else:
		return f"\033[34mDESCONOCIDO ({respuesta.strip()})\033[0m"

def realizar_prueba_binaria(pregunta, contexto, instruccion):
	prompt = crear_prompt_binario(pregunta, contexto, instruccion)
	print(instruccion, f"\033[32m{generador.inferencia(prompt)}\033[0m")

def realizar_prueba_vf(pregunta, contexto, instruccion):
	prompt = crear_prompt_vf(pregunta, contexto, instruccion)
	print(instruccion, resultado_vf(generador.inferencia(prompt)))

def realizar_prueba(pregunta, contexto):
	print(f"\nPREGUNTA: {pregunta}")
	print(f"CONTEXTO: {contexto}")
	#realizar_prueba_vf(pregunta, contexto, "El contexto proporcionado contiene exactamente el dato requerido para responder la pregunta del usuario.")
	#realizar_prueba_vf(pregunta, contexto, "El contexto proporcionado no contiene exactamente el dato requerido para responder la pregunta del usuario.")
	#realizar_prueba_vf(pregunta, contexto, "El contexto proporcionado es claro y bien definido.")


	#realizar_prueba_vf(pregunta, contexto, "El contexto brinda información relacionada a la pregunta.")
	#realizar_prueba_vf(pregunta, contexto, "La pregunta puede responderse facilmente con ese contexto.")
	realizar_prueba_vf(pregunta, contexto, "El contexto no responde a la pregunta.")
	realizar_prueba_vf(pregunta, contexto, "Se requiere información adicional para responder la pregunta ya que el contexto es insuficiente")
	#realizar_prueba_vf(pregunta, contexto, "El contexto contiene información extra.")		
	#realizar_prueba_vf(pregunta, contexto, "El contexto no habla acerca de la pregunta.")		
	#realizar_prueba_vf(pregunta, contexto, "El contexto es necesario para responder la pregunta.")		
	#realizar_prueba_vf(pregunta, contexto, "Con ese contexto no puedo responder la pregunta, pero puedo justificar por qué no puedo responder la pregunta.")


	#realizar_prueba_vf(pregunta, contexto, "Puedo responder satisfactoriamente a la pregunta del usuario solo con la información del contexto proporcionado.")
	#realizar_prueba_vf(pregunta, contexto, "Para responder satisfactoriamente a la pregunta del usuario necesito mas información que la proporcionada en el contexto.")
	#realizar_prueba_vf(pregunta, contexto, "El contexto proporcionado contiene el dato necesario para responder a la pregunta del usuario")
	#realizar_prueba_vf(pregunta, contexto, "Al contexto le falta información esencial para responder a la pregunta del usuario.")
	#realizar_prueba_binaria(pregunta, contexto, "¿el contexto proporcionado contiene el dato necesario para responder a la pregunta del usuario?")
	#realizar_prueba_binaria(pregunta, contexto, "¿el contexto proporcionado NO contiene el dato necesario para responder a la pregunta del usuario?")
	#realizar_prueba_binaria(pregunta, contexto, "¿el contexto proporcionado es RELEVANTE para responder a la pregunta del usuario?")
	#realizar_prueba_binaria(pregunta, contexto, "¿el contexto proporcionado es IRRELEVANTE para responder a la pregunta del usuario?")

def pruebas_cortas():
	realizar_prueba("Como se llama el perro de Carlos?", "El perro de Carlos se llama 'Subzero'")
	realizar_prueba("Como se llama el perro de Carlos?", "El perro de Jorge se llama 'Subzero'")
	realizar_prueba("Como se llama el perro de Carlos?", "El gato de Carlos se llama 'Subzero'")
	realizar_prueba("Como se llama el perro de Carlos?", "El perro de Carlos se llama 'Subzero' y su gato se llama 'Sailor'")
	realizar_prueba("Como se llama el perro de Carlos?", "Carlos no tiene perro.")
	realizar_prueba("Como se llama el perro de Carlos?", "El clima esta excelente.")

def pruebas_largas():
	contexto = """
	La ciudad flotante de Neo-Vesper sufre un apagón energético cada vez que el sistema de seguridad nocturno entra en mantenimiento, dejando las calles a merced de incursiones clandestinas. Ante esta crisis, la facción de los guardianes ha decidido desplegar unidades de combate especializadas para patrullar los sectores críticos. Sol, la reconocida líder de la vanguardia armada, ha sido asignada para asegurar el distrito central junto a su fiel compañero mecánico, mientras que su rival histórica, una entidad conocida en los bajos fondos como la Sombra Escarlata, acecha desde los tejados esperando el momento oportuno para intervenir. Por otro lado, Luna mantiene un perfil mucho más reservado operando desde los laboratorios subterráneos del subnivel 4. Su labor principal consiste en calibrar los núcleos de energía cuántica que alimentan las barreras de contención de la ciudad. Aunque los reportes oficiales indican que Luna trabaja en solitario, circulan fuertes rumores entre los técnicos de guardia sobre un misterioso benefactor anónimo que le provee planos prohibidos de tecnología antigua. A pesar de los constantes altercados con los inspectores del consejo, las instalaciones de Luna se han mantenido intactas gracias a la efectividad de sus protocolos de defensa automatizados. Las tensiones escalaron la semana pasada cuando el consejo directivo aprobó un recorte presupuestario del cuarenta por ciento para el mantenimiento del servicio nocturno, provocando protestas masivas en la Plaza Central. Los gremios de periodistas exigen una auditoría inmediata, señalando que desproteger las calles equivale a condenar a los habitantes. Mientras tanto, en los muelles del este, el sindicato liderado por veteranos de la vieja guardia discute en secreto la posibilidad de declarar una huelga indefinida si las autoridades no restituyen los fondos antes del próximo equinoccio."""

	realizar_prueba("¿Quién es la líder de la vanguardia armada asignada al distrito central?", contexto)
	realizar_prueba("¿Quién le provee planos a Luna?", contexto)
	realizar_prueba("¿Cuál es el código de acceso secreto para desactivar los núcleos de energía cuántica de Luna?", contexto)

if __name__ == "__main__":
	generador = Generador(URL_GENERADOR)

	os.system('')  # Activa los colores ANSI en la terminal de Windows
	print("\033[32m******************************* PRUEBAS *******************************\033[0m")
	pruebas_cortas()
	#print("PRUEBAS LARGAS")
	#pruebas_largas()