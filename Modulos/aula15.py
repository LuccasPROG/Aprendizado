import os
import csv

Caminho =   os.path.join(os.path.dirname(__file__), 'pessoas.csv')

with open(Caminho, 'r') as arquivo:
    leitor = csv.DictReader(arquivo) #lé como arquivo em dicionario


    for i in leitor:
        print(i)


# with open(Caminho, 'r') as arquivo: 
#     leitor = csv.reader(arquivo) #Le como arquivo em lista


#     for i in leitor:
#         print(i)