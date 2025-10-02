#Exercicio - Unir lista
#criar uma funcao zipper, que vai unir duas listas na ordem, obs(usar todos os valores da MENOR lista.)
from itertools import zip_longest 

estados = ['Salvador','Ubatuba','Belo Horizonte']
siglas = ['BA','SP','MG','RJ']

# def zipper(lista1, lista2):#outra forma mais uysando list compretion boa forma
#     intervalo = min(len(lista1), len(lista2))
#     return [
#         (lista1[i], lista2[i]) for i in range(intervalo)
#     ]

# print(zipper(estados, siglas))

# print(list(zip(estados, siglas))) Forma mais facil zip une duas listas começa pela menor lista
print(list(zip_longest(estados, siglas)))# outra forma mais começa pela maior lista