import json
pessoa = {
    'nome': 'Lucas',
    'sobrenome': 'evelinton',
    'enderecos': [
        {'rua': 'R1', 'numero': 32},
        {'rua': 'R2', 'numero': 55},
    ],
    'altura': 1.80,
    'numeros_preferidos': (7, 1),
    'dev': True,
    'nada': None,
}
with open('aula55.json', 'w', encoding='utf8') as arquivo:#salva em JSON
    json.dump(
        pessoa,
        arquivo,
        indent=2)

with open('aula55.json', 'r', encoding='utf8') as arquivo:#Ler  em JSON
    pessoa = json.load(arquivo)
    print(pessoa)