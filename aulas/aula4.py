nome = input('Digite seu nome:')
idade = input('Digite sua idade:')
if nome and idade:
    idade = int(idade)
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')

    if ' ' not in nome:
        print('Seu nome não tem espaços!')
    else:
        print('Seu nome tem espaços!')

    print(f'Sua idade é {idade}')
    if idade >= 18:
        print('Você é maior de idade!')
    else:
        print('Você é menor de idade!')

    print(f'Seu nome tem {len(nome)} letras.')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A ultima letra do seu nome é {nome[-1]}')
else:
    print('Desculpe, você deixou compos vazios.')