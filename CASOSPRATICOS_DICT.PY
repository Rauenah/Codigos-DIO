#Cache de resultados:

#Imagine que você está fazendo cálculos pesados ou acessando uma API. 
#Em vez de repetir a operação, você pode guardar os resultados em um dicionário:

'''cache = {}

def fatorial(n):
    if n in cache:
        return cache[n]
    if n == 0 or n == 1:
        cache[n] = 1
    else:
        cache[n] = n * fatorial(n-1)
    return cache[n]

print(fatorial(5))  # 120
print(cache)        # {0: 1, 1: 1, 2: 2, 3: 6, 4: 24, 5: 120} '''

#Contadores de frequência
#Ótimo para contar quantas vezes algo aparece em uma lista (como palavras em um texto):
#Esse código está contando quantas vezes cada palavra aparece no texto.

'''texto = "python é divertido e python é poderoso"
contador= {} #Criamos um dicionário vazio. 
#Ele será usado para guardar cada palavra como chave e o número de vezes que aparece como valor.

for palavra in texto.split():   #split divide a string em uma lista de palavras, separando pelos espaços
    contador[palavra] = contador.get(palavra, 0) + 1 #get tenta pegar o valor da chave  no dicionário.
    
    print(contador)'''

# Configurações de sistema
#Dicionários são perfeitos para guardar configurações:

config = {
    "tema": "escuro",
    "volume": 70,
    "notificações": True
}
print(config["tema"]) #escuro

#4. Representar objetos simples
#Um DICT pode funcionar como uma estrutura para representar entidades:

usuario = {
    "id": 102,
    "nome": "Marilia",
    "email": "marilia123@hotmail",
    "ativo": True
}

#Mapeamento de funções
#Você pode usar chaves para escolher qual função executar:

def soma(a,b): return a+ b
def subtrair (a,b): return a - b

operações = {
    "soma": soma,
    "subtrair": subtrair
}

print(operações["soma"] (10,5)) #15
print(operações["subtrair"] (10, 5)) #5



