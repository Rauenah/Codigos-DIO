#Imagine que você tem uma lista de e-mails cadastrados e que saber quantos são únicos:

'''emails= ["anafrangoeletrico@gmail.com","joaoarroz@hotmail.com", "anafrangoeletrico@gmail.com", "mariasantos@yahoo.com",
         "claudiosilva@uol.com","joaoarroz@hotmail.com"]
emails_unicos = set (emails)  #joaoarroz@hotmail.com', 'anafrangoeletrico@gmail.com', 'mariasantos@yahoo.com claudiosilva@uol.com'

print(emails_unicos)
print(len(emails_unicos))''' #4

#use set() para remover duplicatas
#Use .strip() para remover duplicatas

#Se quiser garantir que não haja problema com maiusculas/minusculas normalize assim:

emails= ["ANAfrangoeletrico@gmail.com","joaoarroz@hotmail.com", "anaFrangoeletrico@gmail.com", "mariasantos@yahoo.COM",
         "Claudiosilva@uol.com","joaoarroz@hotmail.com"]

#normalizar: remover espaços e deixa tudo em minúsculo

emails_limpos = [email.strip().lower() for email in emails]

#criar conjunto para elimitar duplicatas

emails_unicos = set (emails_limpos)

#Ordenar em ordem alfabetica:

emails_ordenados = sorted(emails_unicos)

print(emails_unicos)
print((emails_ordenados))
print(len(emails_unicos)) 

