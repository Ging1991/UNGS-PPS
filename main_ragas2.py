import os
from sentence_transformers import CrossEncoder

os.system('')

print("Cargando modelo juez Cross-Encoder...")
modelo_juez = CrossEncoder("BAAI/bge-reranker-base")
print("¡Modelo cargado con éxito!\n")

def evaluar_con_reranker(pregunta, contexto):
    score = modelo_juez.predict([pregunta, contexto])
    return float(score)

def mostrar_resultado_coloreado(pregunta, contexto):
    score = evaluar_con_reranker(pregunta, contexto)
    if score > 0.5:
        print(f"\033[32m[SI] Relevante (Score: {score:.4f})\033[0m -> P: {pregunta} | C: {contexto[:40]}...")
    else:
        print(f"\033[31m[NO] Irrelevante (Score: {score:.4f})\033[0m -> P: {pregunta} | C: {contexto[:40]}...")


if __name__ == "__main__":
	mostrar_resultado_coloreado("Como se llama el VS de Sol?", "El VS de Sol se llama 'Goliath'")
	mostrar_resultado_coloreado("Como se llama el VS de Sol?", "La economía global se vio afectada este trimestre por la fluctuación del petróleo.")
	mostrar_resultado_coloreado("Como se llama el perro de Carlos?", "El gato de jorge se llama Gaspar.")
	mostrar_resultado_coloreado("Como se llama el perro de Carlos?", "El perro de jorge se llama Gaspar.")
	mostrar_resultado_coloreado("Como se llama el perro de Carlos?", "El gato de carlos se llama Gaspar.")
	mostrar_resultado_coloreado("Como se llama el perro de Carlos?", "El perro de carlos se llama Gaspar.")
	mostrar_resultado_coloreado("Como se llama el perro de Carlos?", "Carlos no tiene perro.")
	mostrar_resultado_coloreado("Como se llama el perro de Carlos?", "Carlos y gaspar, su perro, fueron al parque a pasear.")
	mostrar_resultado_coloreado("Como se llama el perro de Carlos?", "Jorge no tiene perro pero el de carlos se llama gaspar.")
     