lista = []

lista.append(input('Digite seu Nome:'))

for valor in enumerate(lista):
    lista += valor
    print(valor)