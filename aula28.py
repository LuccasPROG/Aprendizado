# (a1 , a2), (b1,b2) = pessoa.items()

# print(a1, a2)
# print(b1, b2) 
# _________________________________________________________________________
# for key, valor in pessoa.items():
#     print(valor, end=' ')
pessoa = {'nome': 'José', #KWARGS | desempacotamente e empacotamento de nomeados!
          'sobrenome': 'Lucas'
          }

dados_pessoa = {'idade': 18,
                'peso': 120
                }

pessoa_completa = {**pessoa, **dados_pessoa} # cria um dicionario somente!

def mostro_argumentos_nomeados(*args, **kwargs):#Função que mostra valores nomeados
    for k, v in kwargs.items():
        print(k, v)

# mostro_argumentos_nomeados(**pessoa_completa)

configuracoes = { #outro exemplo
    'A1': 1,
    'A2': 2,
    'A3': 3,
    'A4': 4,
    'A5': 5,
                        }
mostro_argumentos_nomeados(**configuracoes)