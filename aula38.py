# Exercícios 
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
#Ordene os produtos por nome decrecente 
#Gere produtos_ordenados_por_nome por deep copy
#Ordene os produtos por preco crecente
#Gere produtos_ordenados_por_preco por deep copy

import copy
from dados import produtos



novos_produtos = copy.deepcopy(produtos)

for produto in novos_produtos:
    produto['preco'] = round(produto['preco'] * 1.10,2)


produtos_ordenados_por_nome = sorted(
    copy.deepcopy(novos_produtos),
    key=lambda item: item['nome'], reverse=True)

produtos_ordenados_por_preco = sorted(
    copy.deepcopy(novos_produtos),
    key=lambda item: item['preco'])


print('-='*20)
print('         Tabela de Preços')
print('-='*20)

for i in produtos_ordenados_por_nome :
    print(f"{i['nome']}     preços: {i['preco']:.2f}")
print()
for i in produtos_ordenados_por_preco :
    print(f"{i['nome']}     preços: {i['preco']:.2f}")
    

