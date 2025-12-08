import matplotlib.pyplot as plt



#entrada de dados

nome_completo = input("Digite o nome completo")
idade= int (input ("Digite a idade"))
peso= float (input("Digite o peso (Kg): "))
altura = float(input("Digite a altura (m): "))
quantidade_de_irmaos = int (input("Digite a qunatidade de irmão: "))
quantidade_de_celulares = int (input("Digite a quantidade de celulares : "))
marca= input ("Digite a marca do carro: ")
modelo = input ("Digite o modelo do carro: ")
nome_do_cachorro = input("Digite o nome do cachorro")

#Saida organizada

print("n--- Dados cadastrados ---")
print(f"nome: {nome_completo}")
print(f"idade: {idade} anos")
print(f"peso: {peso} Kg")
print(f"altura:{altura} m")
print(f"irmãos:{"quantidade de irmãos"}")
print(f"celulares: {quantidade_de_celulares}")
print(f"carros: {marca} {modelo}")
print(f"cachorro: {nome_do_cachorro}")

# 🔹 Salvando os dados em um arquivo TXT
with open("dados_usuario.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("--- Dados cadastrados ---\n")
    arquivo.write(f"Nome: {nome_completo}\n")
    arquivo.write(f"Idade: {idade} anos\n")
    arquivo.write(f"Peso: {peso} Kg\n")
    arquivo.write(f"Altura: {altura} m\n")
    arquivo.write(f"Irmãos: {quantidade_de_irmaos}\n")
    arquivo.write(f"Celulares: {quantidade_de_celulares}\n")
    arquivo.write(f"Carro: {marca} {modelo}\n")
    arquivo.write(f"Cachorro: {nome_do_cachorro}\n")

print("\n✅ Dados salvos no arquivo 'dados_usuario.txt'")


#Gráfico simples comparando irmãos e celulares

categorias = ["irmãos", "celulares"]
valores = [quantidade_de_irmaos, quantidade_de_celulares]

plt.bar(categorias, valores, color= ["blue", "green"])
plt.title(f"Comparação de quantidades - {nome_completo}")
plt.ylabel("Quantidade")
plt.show()