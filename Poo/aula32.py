# Enum -> Enumerações
# Enumerações na programação, são usadas em ocasiões onde temos
# um determinado número de coisas para escolher.
# Enums têm membros e seus valores são constantes.
# Enums em python:
#   - são um conjunto de nomes simbólicos (membros) ligados a valores únicos
#   - podem ser iterados para retornar seus membros canônicos na ordem de
#       definição
# enum.Enum é a superclasse para suas enumerações. Mas também pode ser usada
#   diretamente (mesmo assim, Enums não são classes normais em Python).
# Você poderá usar seu Enum com type annotations, com isinstance e
# outras coisas relacionadas com tipo.
# Para obter os dados:
# membro = Classe(valor), Classe['chave']
# chave = Classe.chave.name
# valor = classe.chave.value
import enum

class Direcoes(enum.Enum):
    DIREITA = 1
    ESQUERDA = 2
# Direcoes = enum.Enum('Direcoes', ['ESQUERDA', 'DIREITA'])
# print(Direcoes(1).name, Direcoes['ESQUERDA'].value)


def mover(direcao):
    if not isinstance(direcao, Direcoes):
        raise ValueError('Direção Não Encontrada !!')

    print(f'Movendo para {direcao.name}' )


mover(Direcoes.ESQUERDA)
mover(Direcoes.DIREITA)

