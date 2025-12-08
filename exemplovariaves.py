
#Problema Exemplo
#Maria da Silva tem 37 anos.
#Seu peso atual é de 68,450Kg e sua altura é 1,65m.
#Ela possui 3 irmãos, 2 celulares, um carro da marca #Chevrolet modelo Onix e um cachorro chamado Marley.
#Declarar as variáveis em Python e apresentar os dados na #saída padrão.


nome_completo = "Maria da Silva"
idade = 37
peso= 68.450
altura= 1.65
quantidade_de_irmaos= 3
quantidade_de_celulares= 2
marca= "Chevrolet"
modelo= "Onix"
nome_do_cachorro= "Marley"
print(nome_completo, idade, peso, altura, quantidade_de_irmaos,quantidade_de_celulares, marca, modelo, nome_do_cachorro)

#EU ESTAVA ERRANDO O CODIGO
#você usou dois-pontos : em vez de igual = em algumas 
# #atribuições de variáveis. 
# Em Python, o correto é usar o sinal de igual (=)para atribuir valores.


#Dica extra: saída mais organizada
#Se quiser deixar a saída mais bonita, você pode usar 
#f-strings:

print(f"Nome: {nome_completo}")
print(f"Idade: {idade} anos")
print(f"Peso: {peso} Kg")
print(f"Altura: {altura} m")
print(f"Irmãos: {quantidade_de_irmaos}")
print(f"Celulares: {quantidade_de_celulares}")
print(f"Carro: {marca} {modelo}")
print(f"Cachorro: {nome_do_cachorro}")


