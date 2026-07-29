class Aluno:
    def __init__(self, nome, idade, nota1, nota2) :
        self.nome = nome
        self.idade = idade
        self.nota1 = nota1
        self.nota2 = nota2

    def calcula_media(self):
        media = ((self.nota1 + self.nota2) / 2)
        return media

    def resultados(self):
        media = self.calcula_media()
        if media >= 7:
            return ('aprovado')
        else:
            return ('reprovado')
            
    def exibir(self):

        print(f'O aluno {self.nome} com a notas {self.nota1} e {self.nota2} foi {self.resultados()} com a media {self.calcula_media()}')

nome = str(input('Digite o seu nome: '))
idade = int(input('Digite sua idade: '))
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
l1 = Aluno(nome, idade, nota1, nota2)
l1.exibir()

