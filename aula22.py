# dados = {'name' : 'Edson',
#          'idade' : 19
#          }
# dados['carga'] = 215
# nome = dados.pop('name')
# print(dados.get('name'))
# print(nome)
# print(dados)



import copy
d1 = {'c1': 1,
        'c2': 2,
        'c3': 400,
        'l1':[1,2,3,4]}

d2 = copy.deepcopy(d1) #valor sem o modulo so faz um copia simples, sem mecher dentro de 
#dicionarios que tem lista ou outras coisas aninhadas
d2['c1'] = 'diego'
d2['l1'][1] = 99999

print(d1)
print(d2)
