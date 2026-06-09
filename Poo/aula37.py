# namedtuples - tuplas imutáveis com nomes para valores
# Usamos namedtuples para criar classes de objetos que são apenas um
# agrupamento de atributos, como classes normais sem métodos, ou registros de
# bases de dados, etc. e usando arquivos csv
# As namedtuples são imutáveis assim como as tuplas.
# https://docs.python.org/3/library/collections.html#collections.namedtuple
# https://docs.python.org/3/library/typing.html#typing.NamedTuple
# from collections import namedtuple
from typing import NamedTuple

class Carta(NamedTuple):
    valor:str = 'valor'
    naipe: str = 'naipe'

as_espada = Carta('A')
# carta = namedtuple('Carta', ['valor', 'naipe'],
#     defaults=['VALOR','NAiPE']                   
# )
# as_espadas = carta('A', '♠️')
# print(as_espadas)
# print(as_espadas.naipe)
# print(as_espadas._fields)

# for valor in as_espadas:
#     print(valor)

print(as_espada._asdict( ))