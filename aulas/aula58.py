# Introdução ao método __init__ (inicializador de atributos)
# As classes geram novos objetos (instâncias) que
# podem ter seus próprios atributos e métodos.
# Os objetos gerados pela classe podem usar seus dados
# internos para realizar várias ações.
# Por convenção, usamos PascalCase para nomes de classes.
class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

p1 = Pessoa('José', 'Lucas')
# p1.nome = 'José'
# p1.sobrenome = 'Lucas'
p2 = Pessoa('Camila', 'oliveira')

p3 = Pessoa('Gaby', 'jesus')
# p2.nome = 'camila'
# p2.sobrenome = 'oliveira' 

# print(p1)
print(p1.nome)
print(p1.sobrenome)
# print(p2)
print(p2.nome)
print(p2.sobrenome)

print(p3.nome)
print(p3.sobrenome)