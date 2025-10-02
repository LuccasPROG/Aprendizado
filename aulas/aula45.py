#Considerando duas listas de inteiros ou float(lista A e lista B)
#Some os valores na lista retornando uma nova lista com os valores somados:
#Se uma lista for maior que a outra, a soma só vai considerar o tamanho da menor.
lista_a = [10, 18, 2, 10, 4, 5, 6, 7]
lista_b = [2, 1, 20, 8]

def zipper(lista1, lista2):#meu jeito de fazer
    menorlista = min(len(lista1), len(lista2))
    return [lista1[i] + lista2[i] for i in range(menorlista)]

#INICIO:
print(zipper(lista_a, lista_b))

# outra forma de fazer mais pytonica

# soma = [x + y for x,y in zip(lista_a, lista_b)]
# print(soma)

#Outra forma de fazer pegando a maior lista

# from itertools import zip_longest
#  #Essa list comprehension pega o maior valor com zip_longest e o fillvalue e os valores faltado se orna 0 
# lista_soma = [x + y for x, y in zip_longest(lista_a, lista_b, fillvalue=0)]
# print(lista_soma)  