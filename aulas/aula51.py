from functools import reduce

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]
# def funcao_do_reduce(acumulador, produto):
#     print(acumulador)
#     return acumulador + produto['preco']


#INicio
total = reduce( #reduce faz a redução de um iterável em um valor
    # funcao_do_reduce, # a funcao outra forma usando lambda
    lambda ac, p: ac + p['preco'],
    produtos, # o parametro
    0 # Valor Inicial
)
print()
print(f'total : {total}')

total = 0
for p in produtos:
    total +=  p['preco']

# print(total)

# print(sum(p['preco'] for p in produtos)) Usando List compreheision