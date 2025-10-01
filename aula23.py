import os   
from time import sleep
perguntas = [
    {
        'Pergunta' : 'Quanto é 2+2?',
        'Opções' : ['1','3','4','5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['10','45','25','15'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4','3','2','5'],
        'Resposta': '5',
    },
]
qtd_acertos = 0
for pergunta in perguntas:
    os.system('cls')
    print('Pergunta',pergunta['Pergunta'])
    print()

    opcoes = pergunta['Opções']

    for i, opcao in enumerate(opcoes):
        print(f"{i}) {opcao}")
    escolha = input('Sua opção:')
    print('Analizando',end='',flush=True)
    print('.',end='',flush=True)
    sleep(0.9)
    print('.',end='',flush=True)
    sleep(0.9)
    print('.',flush=True)
    sleep(0.9)


    acertou = False
    escolha_int = None

    qtd_opção = len(opcoes)

    if escolha.isdigit():
        escolha_int = int(escolha)

    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int < qtd_opção:
            if opcoes[escolha_int] == pergunta['Resposta']:
                acertou = True
    print()
    if acertou:
        print('Acertou✅')
        sleep(1)
        qtd_acertos += 1
    else:
        print('Errou❌')
        sleep(1)
        
    print()
os.system('cls')
print('Encerrando',end='',flush=True)
print('.',flush=True,end='')
sleep(0.9)
print('.',flush=True,end='')
sleep(0.9)

print('.',flush=True)
sleep(0.9)

print(f'Você acertou {qtd_acertos} de {len(perguntas)} perguntas.')
print()