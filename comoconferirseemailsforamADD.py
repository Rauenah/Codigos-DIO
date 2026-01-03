import openpyxl

# Abrir o arquivo salvo

wb = openpyxl.load_workbook("Emails_unicos2.xlsx")
ws= wb["Emails"]

# Ler todos os valores da primeira coluna (onde estão os emails)

emails = []
for row in ws.iter_rows(min_col =1, max_col=1, values_only=True):
    emails.append(row[0])

    # Mostrar os emails
print("Lista completa de emails na planilha:")
for email in emails:
    print(email)