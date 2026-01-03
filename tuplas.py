#uma tupla é uma estrutura de dados que funciona como uma lista,
# mas com uma diferença fundamental: tuplas são imutáveis, ou seja,
#depois de criadas não podem ser alteradas

#Criando Tuplas

#Tupla Simples

numeros = (1,2,3)

#Tupla com tipos diferentes

dados= ("Laura", 25, True)

#Tupla de um único elemento (atenção á virgula)

um_elemento = ("Python")

#Acessando elementos

carros = ("gol", "celta", "pálio")
print(carros[0]) #saida: gol
print(carros[-1]) #saida:palio

#Interando sobre Tuplas
for carro in carros:
    print(carro)

#Diferença entre Tupla e Lista

#Tupla () imutavel, dados fixos, constantes, mais rapido ocupa menos memoria

#Lista [] mutavel, dados mudam ao longo do programa, mais flexível, menos eficiente   