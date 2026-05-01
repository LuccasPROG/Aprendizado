import json
with open('aula6.json', 'r')as arquivo:
    pessoa = json.load(arquivo)

print(pessoa)