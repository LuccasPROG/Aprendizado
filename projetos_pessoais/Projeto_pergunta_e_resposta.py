perguntas = [
    {
        'Pergunta': 'Quanto é 2 + 2?',
        'Opções': ['1','3','4','5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5 * 5?',
        'Opções': ['25', '55','10','51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10 / 2', 
        'Opções': ['4','5','2','1'],
        'Resposta': '5'
    }
]
acertou = 0
contador = 0
while contador < len(perguntas):
    pergunta = perguntas[contador]
    print(f"Pergunta: {pergunta['Pergunta']}")
    print('Opções:')
    for i, opcao in enumerate(pergunta['Opções'],start=1):
        print(f'{i}) {opcao}')    
    opcao = int(input('Opções:'))

    opcao -= 1
    if pergunta['Opções'][opcao] == pergunta['Resposta']:
        print('Acertou👌')
        acertou += 1
        
    else:
        print('Errou❌')

    contador += 1
print(f'Você acertou {acertou} de {len(pergunta)}')