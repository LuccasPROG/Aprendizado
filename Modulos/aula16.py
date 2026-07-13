import csv 
from pathlib import Path

CAMINHO_CSV = Path(__file__).parent / 'pessoas2.csv'

lista_clientes = [
    {'Nome': 'Lucas', 'Endereço': 'av 1, 22'},
    {'Nome': 'xavier', 'Endereço': 'av 3, 44'},
    {'Nome': 'otavio', 'Endereço': 'av 70, 1991'},
]

with open(CAMINHO_CSV, 'w') as arquivo:
    nome_colunas = lista_clientes[0].keys()
    escritor = csv.DictWriter(arquivo,fieldnames=nome_colunas)
    escritor.writeheader()

    for cliente in lista_clientes:
        escritor.writerow(cliente)
# lista_clientes = [ Esse é Linha por linha
#     {'Nome': 'Lucas', 'Endereço': 'av 1, 22'},
#     {'Nome': 'xavier', 'Endereço': 'av 3, 44'},
#     {'Nome': 'otavio', 'Endereço': 'av 70, 1991'},
# ]

# with open(CAMINHO_CSV, 'w') as arquivo:
#     nome_colunas = lista_clientes[0].keys()
#     escritor = csv.writer(arquivo)

#     escritor.writerow(nome_colunas)

#     for cliente in lista_clientes:
#         escritor.writerow(cliente.values())