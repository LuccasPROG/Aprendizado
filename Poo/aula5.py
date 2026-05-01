class Pessoa:
    ano_atual = 2026
    

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


    def Get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade

p1 = Pessoa('Lucas', 20)

print(p1.Get_ano_nascimento())
print(Pessoa.ano_atual)
