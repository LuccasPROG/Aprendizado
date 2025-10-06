#valores Truthy e Falsy, tipos mutaveis e Imutaveis
lista = []
dicionario = {}
conjunto = set()
tupla = ()
string = ''
inteiro = 0
flutuante = 0.0
nada = None
false = False
intervalo = range(0)

def falsy(valor):
    return 'falsy'if not valor else 'truthy'

print('TESTE', falsy('TESTE'))
print(lista, falsy(lista))
print(dicionario, falsy(dicionario))
print(conjunto, falsy(conjunto))
print(tupla, falsy(tupla))
print(inteiro, falsy(inteiro))
print(flutuante, falsy(flutuante))
print(nada, falsy(nada))
print(false, falsy(false))
print(intervalo, falsy(intervalo))