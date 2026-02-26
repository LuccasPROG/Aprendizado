from produtos.produto_modulos import produtos 
import copy

novos_produtos = copy.deepcopy(produtos)

novos_produtos = [{**produto, 'preco': round(produto['preco'] * 1.10, 2)}
                    for produto in novos_produtos ]

Produtos_Ordenado = sorted(copy.deepcopy(novos_produtos), key=lambda a : a['nome'], reverse=True)




print('copia antiga')
print(*produtos, sep='\n')
print()
print('copia nova')
print(*Produtos_Ordenado, sep='\n')

