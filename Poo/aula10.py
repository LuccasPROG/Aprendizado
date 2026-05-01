class Caneta:
    def __init__(self, cor):
        self._cor = cor
        self._cor_tampa = None

##########################################
#   Configuração da cor tranformando um metodo
#   em um atributo !!
    @property
    def cor(self):
        return self._cor

    @property
    def cor_tampa(self):
        return self._cor_tampa

#   configuração  da cor recebendo o valor 
#   
    @cor.setter
    def cor(self, valor):
        self._cor = valor

    @cor_tampa.setter
    def cor_tampa(self, cor):
        self._cor_tampa = cor
##########################################

caneta = Caneta('Azul')
caneta.cor = 'rosa'
caneta.cor_tampa = 'Preto'

print(caneta.cor_tampa)
print(caneta.cor)

##########################################
