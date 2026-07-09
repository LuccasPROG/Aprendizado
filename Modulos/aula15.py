import csv

with open('pessoas.csv', 'r', encoding='utf8') as arquivo:
    leitor = csv.reader(arquivo)

    for linha in leitor:
        print(linha)