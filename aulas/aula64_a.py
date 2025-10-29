import json
from aula64 import CAMINHO_DO_ARQUIVO, Pessoa, fazer_dump

# fazer_dump()
with open(CAMINHO_DO_ARQUIVO, 'r', encoding='utf8') as arquivo:
    pessoas = json.load(arquivo)

    p1 = Pessoa(**pessoas[0])
    p2 = Pessoa(**pessoas[1])

    print(p1.nome, p1.idade)
    print(p2.nome, p2.idade)
