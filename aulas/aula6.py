try:
    numero = int(input('Digite um número:'))
    if numero % 2 == 0:
        print(f'O numero {numero} é par!')
    else:
        print(f'O numero {numero} é impar!')
except(ValueError):
    print('Erro: Digite um Numero Inteiro!')
finally:
    print('>> Volte Sempre <<')