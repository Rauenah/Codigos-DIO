#from → importar coisas prontas.
#def → criar funções.
#datetime.strptime → transformar texto em data.
#timedelta → somar/subtrair tempo em datas.
#return → devolver o resultado de uma função.
#use input() para coletar dados do usuário.
#sempre retorna string → converta se precisar de número.
#torna o programa interativo e flexível.

#def como funciona:
  #def nome_da_função (parametros):
  #instrução 1
  #instrução 2
  #....
  #return valor (opcional)

def calcular_imposto (valor):
  if valor < 1000:
     imposto = valor *0.1
  elif valor <2000:
       imposto = valor  *0.13
  else:
      imposto = valor * 0.2
  return imposto

preco_produto1 = 1500
preco_produto2 = 3500
imposto_produto1 = calcular_imposto (preco_produto1)
imposto_produto2= calcular_imposto(preco_produto2)
print(imposto_produto1)
print(imposto_produto2)

