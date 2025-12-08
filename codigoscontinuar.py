import csv

# Nome dos arquivos
arquivo_txt = "dados_usuario.txt"
arquivo_csv = "dados_usuarios.csv"

# 🔹 Criar o CSV com cabeçalho (apenas uma vez)
with open(arquivo_csv, "w", newline="", encoding="utf-8") as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerow(["Nome", "Idade", "Peso", "Altura", "Irmãos", "Celulares", "Carro", "Modelo", "Cachorro"])

# 🔹 Loop para cadastrar várias pessoas
while True:
    # Entrada de dados
    nome_completo = input("Digite o nome completo: ")
    idade = int(input("Digite a idade: "))
    peso = float(input("Digite o peso (Kg): "))
    altura = float(input("Digite a altura (m): "))
    quantidade_de_irmaos = int(input("Digite a quantidade de irmãos: "))
    quantidade_de_celulares = int(input("Digite a quantidade de celulares: "))
    marca = input("Digite a marca do carro: ")
    modelo = input("Digite o modelo do carro: ")
    nome_do_cachorro = input("Digite o nome do cachorro: ")

    # Saída organizada no terminal
    print("\n--- Dados cadastrados ---")
    print(f"Nome: {nome_completo}")
    print(f"Idade: {idade} anos")
    print(f"Peso: {peso} Kg")
    print(f"Altura: {altura} m")
    print(f"Irmãos: {quantidade_de_irmaos}")
    print(f"Celulares: {quantidade_de_celulares}")
    print(f"Carro: {marca} {modelo}")
    print(f"Cachorro: {nome_do_cachorro}")

    # 🔹 Salvando em TXT (último cadastro sobrescreve)
    with open(arquivo_txt, "w", encoding="utf-8") as arquivo:
        arquivo.write("--- Dados cadastrados ---\n")
        arquivo.write(f"Nome: {nome_completo}\n")
        arquivo.write(f"Idade: {idade} anos\n")
        arquivo.write(f"Peso: {peso} Kg\n")
        arquivo.write(f"Altura: {altura} m\n")
        arquivo.write(f"Irmãos: {quantidade_de_irmaos}\n")
        arquivo.write(f"Celulares: {quantidade_de_celulares}\n")
        arquivo.write(f"Carro: {marca} {modelo}\n")
        arquivo.write(f"Cachorro: {nome_do_cachorro}\n")

    print("\n✅ Dados salvos em 'dados_usuario.txt'")

    # 🔹 Adicionar os dados no CSV (não sobrescreve, acumula)
    with open(arquivo_csv, "a", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow([nome_completo, idade, peso, altura, quantidade_de_irmaos, quantidade_de_celulares, marca, modelo, nome_do_cachorro])

    print("✅ Dados adicionados ao arquivo 'dados_usuarios.csv'")

    # Perguntar se quer cadastrar outra pessoa
    continuar = input("\nDeseja cadastrar outra pessoa? (s/n): ").lower()
    if continuar != "s":
        break

# 🔹 Ler o CSV de volta e mostrar todos os registros
print("\n--- Lista completa de cadastros ---")
with open(arquivo_csv, "r", encoding="utf-8") as arquivo:
    leitor = csv.reader(arquivo)
    cabecalho = next(leitor)
    print("Cabeçalho:", cabecalho)

    for linha in leitor:
        print("Registro:", linha)