#Métodos de classes + factories (fábricas)
#São métodos onde "self" será "cls", ou seja, 
#ao invés de receber a instância no primeiro
#parâmetro, receberemos a própria classe.
class Pessoa:
    ano = 2025 #atributo de classse

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod #<- Isso é uma fabrica   
    def metodo_classe(cls):# cls = propria classe 
        print('hey')

    @classmethod #<- Isso é uma fabrica
    def criar_com_50_anos(cls, nome):# cls = propria classe 
        return cls(nome, 50)

    @classmethod #<- Isso é uma fabrica
    def sem_nome(cls, idade):# cls = propria classe 
        return cls('Anônimo', idade)

p1 = Pessoa('Lucas', 19)
p2 = Pessoa.criar_com_50_anos('Edson')
p3 = Pessoa('Anônimo', 30)
p4 = Pessoa.sem_nome(30)

print(p1.nome, p2.idade)
print(p2.nome, p2.idade)
print(p3.nome, p3.idade)
print(p4.nome, p4.idade)

# print(Pessoa.ano)
# Pessoa.metodo_classe()