from dataclasses import dataclass


@dataclass(init=False)
class Pessoa:
    nome: str
    sobrenome: str
    def __init__(self, nome, sobrenome) -> None:
        self.nome = nome
        self.sobrenome = sobrenome
        self.nome_completo = f'{self.nome} {self.sobrenome}'
        
    # @property
    # def nome_completo(self):
    #     return f'{self.nome} {self.sobrenome}'

    # @nome_completo.setter
    # def nome_completo(self, valor):
    #     nome, *sobrenome = valor.split()
    #     self.nome = nome
    #     self.sobrenome = ' '.join(sobrenome)

if __name__ == "__main__":
    p1 = Pessoa('Lucas', 'ovo')
    # p1.nome_completo = 'Lucca Mandes'
    print(p1)
    print(p1.nome_completo)