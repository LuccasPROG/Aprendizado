# Metodos em instâncias de classes Python
#
class Carro:
    def __init__(self, nome='Sei lá'):
        self.nome = nome
        


    def acelerar(self):
        print(f'{self.nome} está acelerando ...')



fusca = Carro('fusca')
# print(fusca.nome)
fusca.acelerar()
# Carro.acelerar(fusca)

celta = Carro('celta')
# print(celta.nome)
celta.acelerar()
# Carro.acelerar(celta)

camaro = Carro('camaro')
# print(camaro.nome)
camaro.acelerar()
# Carro.acelerar(camaro)