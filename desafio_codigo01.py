n = 3
entradas = [
    "Ana 100",
    "Joao 150",
    "Maria 200"
]

total = 0

for linha in entradas:
    nome, valor = linha.split()
    total += float(valor)

media = total / n

print(f"Total pago em bonus: {total:.0f}")
print(f"Media de bonus: {media:.2f}")