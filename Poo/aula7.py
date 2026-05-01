class Pessoa:
    ano = 2023

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def criar_50_anos(cls, nome):
        return cls(nome, 50)
    
    @classmethod
    def criar_sem_nome(cls, idade):
        return cls('anonimo', idade)
    

# p1 = Pessoa('joao', 25)
p1 = Pessoa.criar_50_anos('lucas')
p2 = Pessoa.criar_sem_nome(15)
print(p1.nome, p1.idade)
print(p2.nome, p2.idade)