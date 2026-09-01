class Chat:

	def __init__(self, chat_bot):
		self.chat_bot = chat_bot

	def comenzar(self):
		print("=== ZEUS: IA CONVERSACIONAL Con RAG, FAISS, LLAMACPP ===")
		print("Escribe 'salir' para finalizar.\n")

		while True:
			print("\n********************************************************************************")
			pregunta = input("\nTu pregunta: ")
			if pregunta.lower() == "salir":
				break
				
			if not pregunta.strip():
				continue

			try:
				respuesta = self.chat_bot.consultar(pregunta)
				print("\n--- Respuesta del Asistente ---")
				print(f"- ZEUS: {respuesta}")
			except Exception as e:
				print(f"\n[ERROR]: {e}")