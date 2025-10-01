nome = str(input('Digite seu Primeiro Nome:'))

if len(nome) <= 4:
    print(f'Seu nome {nome} é curto!')
elif len(nome) <= 6:
    print(f'Seu Nome {nome} é Normal!')
else:
    print(f'Seu Nome {nome} é Muito grande!')