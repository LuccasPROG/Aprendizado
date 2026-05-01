class multiplicador:
    def __init__(self, multiplicador):
        self.multiplicador = multiplicador
    
    def multiplicar(self, numero):
        return self.multiplicador * numero
    

dobro = multiplicador(2)
print(dobro.multiplicar(9))
