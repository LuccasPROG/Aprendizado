class Pergunta:
    def __init__(self, pergunta, opcao, resposta):
        self.pergunta = pergunta
        self.opcao = opcao
        self.resposta = resposta

class Quiz:
    def __init__(self, perguntas):
        self.perguntas = perguntas
        self.acertos = 0
    

    def _Main(self):

        contador = 0
        while contador < len(self.perguntas):
            pergunta = self.perguntas[contador]

            print(pergunta.pergunta)
            print('Opções:')

            for i, opcao in enumerate(pergunta.opcao, start=1):
                print(f'{i}) {opcao}')
            escolha = int(input('Digite sua Opção: '))
            escolha -= 1

            if pergunta.opcao[escolha] == pergunta.resposta:
                print('Acertou👌')
                self.acertos += 1
            else:
                print('Errou❌')



            contador += 1

        print(f'Você acertou {self.acertos} de {len(self.perguntas)}')

#INICIO
p1 = Pergunta('Quanto é 2 + 2?',
              ['1','3','4','5'],
              '4',)
p2 = Pergunta('Quanto é 5 * 5?',
              ['25', '55','10','51'],
              '25',)
p3 = Pergunta('Quanto é 10 / 2', 
              ['4','5','2','1'],
              '5')

quiz = Quiz([p1,p2,p3])
quiz._Main()

