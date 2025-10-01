try:
    horario = float(input('Digite seu horario agora:'))
    if horario >= 0 and horario <= 11:
        print(f'É {horario} bom Dia!')
    elif horario >= 12 and horario <= 17:
        print(f'É {horario:.2f} e boa Tarde!')
    elif horario >= 18 and horario <= 23:
        print(f'É {horario:.2f} e boa Noite!')
    else:
        print('Não conheço essa hora !')
except(ValueError):
    print('Digite um Numero inteiro!')
finally:
    print('>> Volte sempre <<')
