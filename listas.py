#Listas são estruturas de dados que permitem armazenar múltiplos valores em uma única variável.
#Elas são coleções ordenadas e mutáveis, ou seja:

#Ordenadas → os elementos mantêm a posição em que foram inseridos.
#Mutáveis → você pode alterar, adicionar ou remover itens depois de criar a lista.
#São delimitadas por colchetes  e os elementos são separados por vírgulas.


#Possuem muitos métodos úteis, como:
# → adiciona no fim              .APPEND()
# → insere em posição específica .INSERT()
# → remove um item               .REMOVE()
# → remove pelo índice           .POP()
# → ordena a lista               .SORT()
# → inverte a ordem              .REVERSE()
# → Serve para retornar o número de itens em um objeto .len()


#Exemplo básico:

#Criando uma lista

frutas = ["maça", "banana", "laranja"]
          
#Acessando elementos (indices começam em 0)

print(frutas[0])  # saída: maçã
print(frutas[2])  # saída: laranja

#Alterando elementos

frutas [1] = "uva"
print (frutas) #saída: ["maçã", "uva", "laranja"]

#Adicionando elementos

frutas.append("abacaxi")
print(frutas) # saída: ["maçã", "uva", "laranja", "abacaxi"]

#Removendo elementos

frutas.remove("uva")
print(frutas) # saída: ["maçã", "laranja", "abacaxi"]


#Podem conter tipos diferentes de dados

lista_mista = [1, "texto", 3.14, True]

#Aceitam valores repetidos

numeros= [1,2,2,3]

#Len  Serve para retornar o número de itens em um objeto

#com listas

frutas = ["maçã", "banana", "laranja"]
print(len(frutas))  # saída: 3

#com string

texto = "Python"
print(len(texto))  # saída: 6

#com tuplas

numeros = (10, 20, 30, 40)
print(len(numeros))  # saída: 4





