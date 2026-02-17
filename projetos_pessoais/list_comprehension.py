Produtos = [
    {'nome': 'p1', 'preco': 10},
    {'nome': 'p2', 'preco': 20},
    {'nome': 'p3', 'preco': 30},
    {'nome': 'p4', 'preco': 184},
]
# novos_produtos = [{**produto, 'preco': produto['preco'] * 1.05 }#MAPEAMENTO ANTES DO FOR
#                   if produto['preco'] > 20 else {**produto}    #serve para mudar coisas
#                    for produto in Produtos]

novos_produtos = [{**produto, 'preco': produto['preco'] * 1.05 }#FILTRO serve para remover coisas
                  if produto['preco'] > 20 else {**produto}# Depois do FOR
                   for produto in Produtos if produto['preco'] > 10]


print(*novos_produtos, sep='\n')


# print(novos_produtos)