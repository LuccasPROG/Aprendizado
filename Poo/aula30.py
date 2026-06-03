
def meu_repr(self):
     return f'({type(self).__name__}{self.__dict__})'

class Meta(type):
    def __new__(mcs, name, bases, dct):
        print('METACLASS New')
        cls = super().__new__(mcs, name, bases, dct)
        cls.attr = 123456
        cls.__repr__ = meu_repr

        if 'falar' not in cls.__dict__:
            raise NotImplementedError('implemente falar')

        return cls
    
    def __call__(self, *args, **kwds):
        instancia = super().__call__(*args, **kwds)
        
        if 'nome' not in instancia.__dict__:
             raise NotImplementedError('Crie o attr nome')

        return instancia

class Pessoa(metaclass=Meta):
    def __new__(cls, *args, **kwargs):
        print('Meu New')
        instancia = super().__new__(cls)
        return instancia
    
    def __init__(self, nome):
            print('Meu Init')
            # self.nome = nome

    def falar(self):
        print('Falando. .. ')
        

p1 = Pessoa('Luiz')
print(p1.attr)
print(p1)