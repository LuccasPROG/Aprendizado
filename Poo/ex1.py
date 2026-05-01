class Arma:
    def __init__(self, nome):
        self.nome = nome

    def atacar(self):
        return f'{self.nome} Atacou!'

class Jogador:
    def __init__(self,nome):
        self.nome = nome
        self.arma = None

espada = Arma('Espada')
jogador = Jogador('Lucas')

jogador.arma = espada

print(jogador.arma.atacar())