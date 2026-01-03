# O que esse código faz
#1. 	Normaliza todos os emails ( strip() e lower()
#2. 	Remove duplicatas com set()
#3. 	Ordena alfabeticamente com sorted()
#4. 	Cria uma planilha Excel usando openpyxl.
#5. 	Adiciona os emails únicos em uma coluna chamada Emails.
#6. 	Salva o arquivo como emails_unicos

import csv

#lista original de emails

emails=[
    "ANAfrangoeletrico@gmail.com",
    "joaoarroz@hotmail.com",
    "anaFrangoeletrico@gmail.com",
    "mariasantos@yahoo.COM",
    "Claudiosilva@uol.com",
    "joaoarroz@hotmail.com"
]

#1. # 1. Normalizar (remover espaços e deixar tudo minúsculo)
emails_limpos =[email.strip().lower() for email in emails]

# 2. Remover duplicatas e ordenar
emails_unicos= sorted(set(emails_limpos))

# 3. Criar e salvar arquivo CSV

with open("emails_unicos.csv", "w", newline="", encoding ="utf-8") as arquivo:
    escritor =csv.writer(arquivo)

    # Cabeçalho
    escritor.writerow(["Emails"])
   
    # Linhas com os emails
    for email in emails_unicos:
        escritor.writerow([email])

print("Arquivo CSV criado com sucesso!"
)        


#CSV (Comma-Separated Values)
#• 	Formato: Texto simples, cada linha representa um registro e os campos são separados por vírgula (ou outro delimitador, como ponto e vírgula).
#• 	Leve: Arquivos pequenos e fáceis de abrir em qualquer editor de texto.
#• 	Compatibilidade: Funciona em praticamente todos os sistemas, bancos de dados e planilhas.
#• 	Limitações:
#• 	Não guarda formatação (cores, negrito, bordas).
#• 	Não suporta múltiplas abas (só uma tabela por arquivo).
#• 	Não armazena fórmulas, apenas valores.



