#Um dicionário é como uma tabela de correspondência: você procura algo pela chave e obtém o valor.
#Sintaxe: usa chaves {} e pares separados por dois pontos (:)

pessoa = {
    "nome": "Paulo",
    "idade":29,
    "filhos":["João", "Maria"]
}
print(pessoa["filhos"])  #Joao, Maria  #Aqui "nome", "idade" e "filhos" são chaves, e "Paulo", 29, ["João", "Maria"] são os valores

for filho in pessoa ["filhos"]:  #Se você quiser imprimir cada filho separadamente
    print(filho)


#⚡ Características principais

#Chaves únicas: não podem se repetir.
#Valores flexíveis: podem ser números, strings, listas, outros dicionários etc.
#Acesso rápido: buscar por chave é muito eficiente (complexidade O(1)).
#Mutáveis: você pode adicionar, remover ou alterar pares chave-valor.

#OPERAÇÕES COMUNS:

#CRIAR DICIONARIO:

carro = {"Marca": "Ford", "Modelo": "Fiesta", "Ano": 2015}

# CRIAR DICIONARIO:
carro = {"Marca": "Ford", "Modelo": "Fiesta", "Ano": 2015}

# ACESSAR VALOR PELA CHAVE:
print(carro["Marca"])  # Ford

# ADICIONAR NOVO PAR:
carro["cor"] = "azul"

# ALTERAR VALOR EXISTENTE:
carro["Ano"] = 2020   # aqui está a correção

# REMOVER PAR:
del carro["Modelo"]

print(carro)

#COMPARAÇÃO COM OUTRAS ESTRUTURAS:

#LISTA: indice numericos(0,1,2...) QUANDO USAR: Sequencia ordenada de elementos
#TUPLA: igual á lista, mas imutavel QUANDO USAR: Dados fixos que não mudam
#CONJUNTO SET: elementos unicos, em ordem QUANDO USAR: Remover duplicatas, operações matematicas
#DICIONARIO: pares chave-valor QUANDO USAR: mapear relações(ex: produto >> preço, aluno>>nota)
