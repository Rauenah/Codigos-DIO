#Como abrir planilha existente e adicionar novos emails

import openpyxl

#Abrir o arquivo existente

wb= openpyxl.load_workbook("Emails_unicos2.xlsx")
ws= wb["Emails"] #seleciona a aba chamada "Emails"

#Lista de novos emails que você quer adicionar

novos_emails=[
    "mariajoaquina@hotmail.com",
    "seltonmello@yahoo.com",
    "lauracardoso@gmail.com"
]

#Ler todos os emails já existentes na planilha coluna A)

emails_existentes = set()
for row in ws.iter_rows(min_col =1, max_col =1, values_only= True):
    if row[0]: #evita células vazias

        emails_existentes.add(row[0].strip().lower())  # usa row[0], não 'email'

  # normaliza para evitar duplicatas por maiúsculas/minúsculas


#Inserir novos emails a partir da próxima linha
for email in novos_emails:
    if email.strip().lower() not in emails_existentes:
        ws.append([email])  # adiciona na próxima linha disponível

        emails_existentes.add(email.strip().lower())  # atualiza o conjunto


#Salvar novamente o arquivo

wb.save("Emails_unicos2.xlsx")    
print("Novos emails salvos com sucesso sem duplicatas")


#Se voce quiser adicionar sempre na última linha disponivel use:

#for email in novos_emails:
    #ws.append([email])Quer que eu te mostre também como ler de volta os emails para confirmar que foram adicionados corretamente?