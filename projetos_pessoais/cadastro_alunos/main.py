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

def validacao_notas():
    while True:
        nota = float(input('Digite a nota: '))
        if 0 <= nota <= 10:
            return nota
        else:
             print('Nota invalida: digite uma nota entre 0 e 10 !')

#Inicio

nome = str(input('Digite o seu nome: '))
idade = int(input('Digite sua idade: '))
nota1 = validacao_notas()
nota2 = validacao_notas()
l1 = Aluno(nome, idade, nota1, nota2)
l1.exibir()

