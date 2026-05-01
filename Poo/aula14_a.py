#Composição!!
class Carro:
    def __init__(self, nome, motor, fabricante):
        self.nome = nome
        self.motor = motor
        self.fabricante = fabricante
       
    
    def exibir(self):
        print(self.nome, self.motor.motor, self.fabricante.fabricante)

class Motor():
    def __init__(self, motor):
        self.motor = motor

class Fabricante:
    def __init__(self, fabricante):
        self.fabricante = fabricante

motor1 = Motor('V8')
fabric1 = Fabricante('Lamborhni')

carro1 = Carro('lucas', motor1, fabric1)

carro1.exibir()
