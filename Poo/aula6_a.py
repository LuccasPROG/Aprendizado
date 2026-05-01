import json
CAMINHO_ARQUIVO = 'aula6.json'


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

informacao_pessoa_1 = Pessoa('jose', 19)
informacao_pessoa_2 = Pessoa('edna', 19)
informacao_pessoa_3 = Pessoa('suelen', 1975)
informacao_pessoa_4 = Pessoa('Josue', 1)

pessoa = [informacao_pessoa_1.__dict__, 
          informacao_pessoa_2.__dict__, 
          informacao_pessoa_3.__dict__,
          informacao_pessoa_4.__dict__]


with open(CAMINHO_ARQUIVO, 'w') as arquivo:
    json.dump(pessoa, arquivo, ensure_ascii=False, indent=2)