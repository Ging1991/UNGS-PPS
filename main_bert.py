from bert_score import score

candidatos = [
    "El VS de Sol se llama Goliath y es un arma muy poderosa.", # Contexto correcto
    "Carlos y Gaspar, su perro, fueron a pasear al parque.", # Contexto correcto
    "La economía global se vio afectada por el petróleo."        # Contexto basura
]

referencias = [
    "El VS de Sol se llama Goliath.",
    "El perro de Carlos se llama Gaspar",
    "El VS de Sol se llama Goliath."
]

# Usamos el parámetro rescale_with_baseline=True para forzar una separación real de scores
P, R, F1 = score(
    candidatos, 
    referencias, 
    lang="es", 
    rescale_with_baseline=True, 
    verbose=False
)

for i, (cand, ref) in enumerate(zip(candidatos, referencias)):
    print(f"\n--- Prueba {i+1} ---")
    print(f"Contexto:     {cand[:45]}...")
    print(f"BERTScore F1: {F1[i].item():.4f}")