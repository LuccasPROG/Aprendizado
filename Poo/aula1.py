class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

p1 = Pessoa('jose', 'Lucas')
# p1.nome = ('Jose')
# p1.sobrenome =  ('lucas')

print(p1.nome)
print(p1.sobrenome)