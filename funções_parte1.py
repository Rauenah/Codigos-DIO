#O que são funções em Python?

#Funções são blocos de código que você pode reutilizar sempre que precisar.
#Elas servem para organizar o programa, evitar repetição e deixar o código mais fácil de entender.
#Pense nelas como uma receita: você dá um nome, define os ingredientes (parâmetros) e o que vai ser feito (corpo da função).

#Em Python usamos a palavra-chave def:

def saudação():
    print("Aprender Python é muito gratificante")

saudação()

# def → define a função
#saudacao → nome da função
#() → pode receber informações (parâmetros)
#O código dentro dela só roda quando você chama a função:
      #saudação()

#FUNÇÕES COM PARÂMETROS:

def soma(a,b):
    return a+b
print (soma(3,5))  #8    

#FUNÇÃO COM VALOR PADRÃO:

def soma(a,b):
    return a +b 
print(soma(3,5))  #8

#EXEMPLO PRÁTICO:

def calcular_media(notas):
    return sum(notas) / len(notas)

aluno1 = [7, 8, 9]
aluno2 = [6, 5, 7]

print(calcular_media(aluno1))  # 8.0
print(calcular_media(aluno2))  # 6.0

#O QUE SÃO ARGS E KWARGS:

# → permite passar vários argumentos posicionais (sem precisar saber quantos).
# → permite passar vários argumentos nomeados (chave=valor).
#Eles são usados quando você quer que sua função seja flexível
# aceitando diferentes quantidades de parâmetros.

#Exemplos: ARGS
#AQUI A FUNÇÃO ACEITA QUALQUER NÚMERO DE VALORES SEM PRECISAR DEFINIAR TODOS

def soma(*args):
    return sum(args)

print(soma(1,2,3))  #6
print(soma(10,20,30,40)) #100

#Usando KWARGS (argumentos nomeados)
#AQUI A FUNÇÃO ACEITA QUALQUER NÚMERO DE PARES CHAVE = VALOR

def mostrar_info(**kwargs):
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")


mostrar_info(nome="Ana", idade=25, cidade = "São Paulo")
#nome: Ana
#idade =25
#cidade: São Paulo

#MISTURANDO ARGS E KWARGS

def exemplo(*args, **kwargs):
    print("args:", args)
    print("kwargs:", kwargs)

exemplo(1, 2, 3, nome="Carlos", ativo=True)
# args: (1, 2, 3)
# kwargs: {'nome': 'Carlos', 'ativo': True}


#Onde usar
#Quando você não sabe quantos argumentos vão ser passados.
#Em funções genéricas que precisam ser reutilizadas em diferentes situações.
#Em bibliotecas e frameworks (como Django ou Flask), onde funções recebem muitas opções configuráveis.
#Para criar funções que lidam com parâmetros opcionais sem complicar.