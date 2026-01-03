# 	O DICT é um tipo de dado nativo em Python.
#Representa um mapeamento entre uma chave única e um valor associado.
#Pode ser criado de duas formas:
# USANDO CHAVES {}:

#EXEMPLO

# CADASTRO SIMPLES:

usuario = dict(nome = "Ana", idade = 25, cidade= "São Paulo")
 
#ACESSANDO CADASTRO:

print(usuario["nome"]) #Ana
print(usuario.get("email", "não informado")) #não informado

#ATUALIZANDO

usuario["idade"] = 26
usuario.update({"email": "ana@gmail.com"})
print(usuario["email"]) #ana@gmail.com

#Iterando

#Iterar em Python significa percorrer elementos de uma coleção (como listas, tuplas, dicionários) 
#ou repetir um bloco de código várias vezes, usando estruturas como for e while, 
#para acessar ou manipular seus itens um por um, de forma eficiente e automatizada. 
#É a base para processar sequências de dados e realizar tarefas repetitivas sem escrever o mesmo código repetidamente, 
#com o for sendo ideal para sequências e o while para condições. 

for chave, valor in usuario.items():
    print(chave, ";", valor)

  # Comparação com outras estruturas
  
#LIST: coleção ordenada de itens
#TUPLE: coleção imutável
#SET: coleção de duplicatas
#DICT: mapeamento chave-valor

#RESUMO:

#DICT  é a ferramenta certa quando você precisa associar informações de forma clara e acessá-las rapidamente por uma chave 
#como um mini banco de dados dentro do seu programa.