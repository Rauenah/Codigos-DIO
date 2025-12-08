#Os operadores de comparação em Python são usados para #comparar valores e retornam sempre um resultado booleano #(True ou False). Eles são: ==, !=, >, <, >=, <=

#  == → Verifica se dois valores são iguais
# != → Verifica se dois valores são diferentes
# > → Retorna True se o valor da esquerda for maior que o da direita.
# < → Retorna True se o valor da esquerda for menor que o da direita.
# >= → Retorna True se o valor da esquerda for maior ou igual ao da direita.
# <= → Retorna True se o valor da esquerda for menor ou igual ao da direita.

#IGUALDADE

5 == 5 #TRUE
5 == 6 #FALSE

#DIFERENÇA

5 != 5 #FALSE
5 != 5 #TRUE

#MENOR QUE

3 < 7 #TRUE
7< 7  #TRUE

#MAIOR QUE

7 > 3 #TRUE
7 > 8 #FALSE

#ONDE USAR: ESTRUTURAS CONDICIONAIS (IF, ELIF, ELSE):

idade = int (input("Escreve sua idade "))
if idade >= 18:
    print("Você é maior de idade ")
else:
    print("Você é menor de idade")


