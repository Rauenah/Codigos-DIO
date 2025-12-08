nome= input("Informe seu nome: ")
idade= input("Informe sua idade ")
salario= float(input("Qual o seu salario"))

# print(type(salario)) quando quero saber o tipo de class

#como solicitar a senha do usuario sem a senha aparecer:

from getpass import getpass

senha = getpass("Qual sua senha: ")
print("Senha digitada com sucesso! ")