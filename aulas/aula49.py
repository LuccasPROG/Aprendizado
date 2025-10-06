# map, partial, GeneratorType e esgotamento de Iterators

# map - para mapear dados
from functools import partial #functools biblioteca que ajuda funções
from types import GeneratorType #verifica se é um Generator


produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]
def aumentar_porcetagem(valor, porcentagem):
    return round(valor * porcentagem, 2)# 2 aumenta a casa decimais

aumenta_dez_porcento = partial(
    aumentar_porcetagem,
    porcentagem=1.1
)

# novos_produtos = [# map - Mapeamento!   bruto
#     {**p, 'preco': aumenta_dez_porcento(p['preco'])} 
#     for p in produtos
# ]

def mudar_preco_produto(produto):
    return {
        **produto,
          'preco': aumenta_dez_porcento(produto['preco']
        )
}
 #maps
novos_produtos = list(map(
    mudar_preco_produto,
    produtos
    )            
)

for i in produtos:
    print(i)
print()

for i in novos_produtos:
    print(i)
print()

print(novos_produtos)

print(# utilizando maps !
    list(map(
    lambda x: x *3,
    [1,2,3,4]
))
)


# print(novos_produtos)
# print(hasattr (novos_produtos, '__iter__'))#verifica se e um iteretor é iteretor se tiver iter e nex == True
# print(hasattr (novos_produtos, '__next__'))

# print(isinstance(novos_produtos, GeneratorType))#verifica se e um generator