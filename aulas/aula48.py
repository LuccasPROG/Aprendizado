# groupby - agrupando valores (itertools)
# O groupby é útil quando você quer agrupar elementos com alguma característica em comum. 
# Exemplos reais:
# Agrupar alunos por nota (como aqui)
# Agrupar vendas por produto
# Agrupar palavras iguais em um texto para contar frequência
# Agrupar arquivos por tipo ou data

from itertools import groupby

alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'André', 'nota': 'A'},
    {'nome': 'Anderson', 'nota': 'C'},
]
def ordena(aluno):
    return aluno['nota']

alunos_agrupado = sorted(alunos, key=ordena)

grupos = groupby(alunos_agrupado, key=ordena)

for chave, grupo in grupos:
    print(chave)
    for aluno in grupo:
        print(aluno)