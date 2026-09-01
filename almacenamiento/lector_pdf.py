import os
import re
from pypdf import PdfReader

class LectorPDF:

	def __init__(self, direccion):
		self.direccion = direccion
		if not os.path.exists(direccion):
			raise FileNotFoundError(f"No se encontraron datos en '{direccion}'.")
		
	def extraer_texto(self):
		PDF = PdfReader(self.direccion)
		texto = ""
			
		for i, pagina in enumerate(PDF.pages):
			contenido = pagina.extract_text()
			if contenido:
				texto += f"\n[Página {i+1}]\n{contenido}"

		texto_sin_saltos = texto.replace('\n', ' ')
		texto_limpio = re.sub(r' +', ' ', texto_sin_saltos)
		return texto_limpio