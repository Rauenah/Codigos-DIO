#and >> todas as condições são VERDADEIRAS
#OR >> pelo menos uma é VERDADEIRA
#NOT >> inverte o resultado lógico

#AND Retorna TRUE SE TODAS AS CONDIÇÕES FOREM VERDADEIRAS

x = 5
print (x > 2 and x < 10)  # True (porque 5 é maior que 2 e menor que 10)

#OR Retorna TRUE se pelo menos uma condição for verdadeira.

X = 5
print (x > 2 or x > 10) # True (porque 5 é maior que 2, mesmo 5 não sendo maior que 10)

#not - Inverte o valor lógico: True vira False, e False vira True.

x = 5
print(not(x > 2))         # False (porque x > 2 é True, mas o not inverte)


#EXEMPLOS

#Verificar se idade está dentro de um intervalo

idade = 20
if idade >= 18 and idade <= 30:
    print("Idade entre 18 e 30 anos")



#Verificar se usuário digitou valor válido
valor = 50
if valor < 0 or valor > 100:
    print("Valor inválido")


#Negação
logado = False
if not logado:
    print("Usuário não está logado")




