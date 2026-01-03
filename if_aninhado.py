#“Aninhado” = uma coisa dentro da outra.
#Pode ser loop, função, estrutura de dados ou condição. 
#É muito usado quando precisamos organizar lógica mais complexa.

#Aqui você define o tipo de conta e os valores de saldo, saque e cheque especial.
#Variaveis iniciais
conta_normal = False
conta_universitaria = False

saldo = 2000
saque = 2500
cheque_especial = 450

#Estrutura principal
#Esse é o primeiro nível de decisão: qual tipo de conta está ativo.
#Se for conta normal → entra no primeiro bloco.
#Se for conta universitária → entra no segundo bloco.
#Se nenhum dos dois → cai no ELSE


if conta_normal:
    if  saldo >= saque:
         print("Saque realizado com sucesso! ")
    elif saque <= (saldo  + cheque_especial):
         print("Saque realizado com uso do cheque especial")
    else:
        print("Não foi possivel realizar saque, saldo insuficiente")   
#Aqui temos um if aninhado:
#Primeiro verifica se é conta normal.
#Dentro desse bloco, faz uma nova verificação sobre saldo e cheque especial.
#O mesmo acontece no bloco da conta universitária:

elif conta_universitaria:
     if saldo >= saque:
        print("Saque realizado com sucesso")   
     else:
        print("Saldo insuficiente! ")  

else:
    print("Sistema não reconhece esse tipo de conta, entre em contato com seu gerente. ")                


#Isso é útil quando você precisa tomar decisões em camadas, 
#primeiro uma condição geral e depois condições específicas.
       

