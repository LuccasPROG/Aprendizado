class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
    
    @property
    def falar_nome_classe(self):
        print(self.nome, self.sobrenome, self.__class__.__name__)

class Cliente(Pessoa):
    ...


class Aluno(Pessoa):
    ...


c1 = Cliente('Lucas', 'Comedor')
c1.falar_nome_classe

a1 = Aluno('Carlos','Oliveira')
a1.falar_nome_classe
