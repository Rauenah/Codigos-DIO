#elif condições alternativas

#if → testa a primeira condição.
#elif → testa uma condição alternativa, caso o if seja falso.
#else → executa se nenhuma das condições anteriores for verdadeira.

nota = 95
if nota >= 90:
    print("Excelente")
elif nota >= 70:
    print("Bom")
elif nota >= 50:
    print ("Regular")
else:
    print("Insuficiente")