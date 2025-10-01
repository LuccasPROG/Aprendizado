#list comprehension uma forma rapida de crir listas!

#                       -> print(list(range(10)))

lista1 = [] # mesma coisa que em cima ^
for numero in range(10): #           |
    lista1.append(numero)
# print(lista)

numerados = [numero for numero in range(10)]  # mesma coisa de cima ^^
# print(numerados)                           #                            ||
#________________________________________________________
# mapeamento de dados em list comprehension o IF é antes do for ! 
import pprint

def p(argumento):
    pprint.pprint(argumento) 
    
produtos = [
    {'nome': 'p1', 'preco': 20,},
    {'nome': 'p2', 'preco': 10,},
    {'nome': 'p3', 'preco': 30,},
]
novo_produto = [
    {**produto, 'preco': produto['preco'] * 1.05} 
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
]
# print(*novo_produto, sep='\n') #form abasica formatada
# pprint.pprint(novo_produto) #Print bonito
# p(novo_produto)
#_________________________________________________________
# filtro de dados em list comprehension o if é depois do for
#pode juntar filtro e mapeamento juntos no caso antes do for e depois tbm
lista2 = [n for n in range(10) if n < 5]
# print(lista2)

#_______________________________________________________________________________
#List comprehension com mais de um For

lista = list()
for x in range(3):
    for y in range(3):
        lista.append((x,y))
# print(lista)
#fazendo isso acima com list comprehension
lista = [
    (x,y)
    for x in range(3)
    for y in range(3)
]

print(lista)