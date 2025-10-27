#__dict__ e vars para atributos de instancia
class Pessoa:
    ano_atual = 2025

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade
dados = {'nome': 'amanda', 'idade': 18}
p1 = Pessoa(**dados)

# p2 = Pessoa('Lucas', 18)

# p1.__dict__['nome'] = 'Eita'
# p1.__dict__['Comida'] = 'Macarrao'
# del p1.__dict__['nome']
# print(p1.__dict__)

# print(vars(p1))

print(p1.nome,end=' ')
print(p1.idade)