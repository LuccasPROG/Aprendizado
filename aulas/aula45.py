#Considerando duas listas de inteiros ou float(lista A e lista B)
#Some os valores na lista retornando uma nova lista com os valores somados:
#Se uma lista for maior que a outra, a soma só vai considerar o tamanho da menor.
lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]

def zipper(lista1, lista2):
    menorlista = min(len(lista1), len(lista2))
    return [lista1[i] + lista2[i] for i in range(menorlista)]

#INICIO:
print(zipper(lista_a, lista_b))