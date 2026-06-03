
def meu_repr(self):
    class_name = type(self).__name__
    class_dict = self.__dict__
    class_repr = f'{class_name}({class_dict})'
    return class_repr


def adiciona_repr(cls):
    cls.__repr__ = meu_repr
    return cls


def meu_planeta(metodo):
    def interno(self, *args, **kwargs):
        resultado = metodo(self, *args, **kwargs)

        if 'Terra' in resultado:
            return('Você não é um alienigine')
        
        return resultado
    return interno


# class MyReprMixin:
#     def __repr__(self):
#         class_name = type(self).__name__
#         class_dict = self.__dict__
#         class_repr = f'{class_name}({class_dict})'
#         return class_repr


@adiciona_repr
class Time:
    def __init__(self, nome):
        self.nome = nome


@adiciona_repr
class Planeta:
    def __init__(self, nome):
        self.nome = nome

    @meu_planeta
    def falar_nome(self):
        return f'O planeta é {self.nome}'
    

brasil = Time('Brasil')
portugal = Time('Portugal')

terra = Planeta('Terra')
neturno = Planeta('Neturno')
Plutao = Planeta('Plutão')

print(brasil)
print(portugal)
print()
# print(terra)
# print(neturno)
# print(Plutao)
print()
print(terra.falar_nome())
print(neturno.falar_nome())
print(Plutao.falar_nome())