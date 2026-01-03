#Primeiro, instale a biblioteca openpyxl se ainda não tiver:
# pip install openpyxl


import openpyxl

# Lista original de emails

Emails=["ANAfrangoeletrico@gmail.com",
    "joaoarroz@hotmail.com",
    "anaFrangoeletrico@gmail.com",
    "mariasantos@yahoo.COM",
    "Claudiosilva@uol.com",
    "joaoarroz@hotmail.com",
     "mateusdejesus@gmail.com"

]

# 1. Normalizar (remover espaços e deixar tudo minúsculo)

Emails_limpos = [email.strip().lower() for email in Emails]

# 2. Remover duplicatas com set()

Emails_unicos = sorted(set(Emails_limpos))   # já ordena alfabeticamente

# 3. Criar uma nova planilha Excel

wb = openpyxl.Workbook() #wb:Workbook representa arquivo inteiro
ws = wb.active           #ws:Worksheet representa uma aba dentro do planilha
ws.title = "Emails"

# 4. Adicionar cabeçalho

ws["A1"] = "Emails"

# 5. Inserir os emails únicos na coluna A

for i, Email in enumerate(Emails_unicos, start=2): # começa na linha 2
    ws[f"A{i}"] = Email

 # 6. Salvar o arquivo

wb.save("Emails_unicos2.xlsx")   
print("Arquivo Excel criado com sucesso !")







