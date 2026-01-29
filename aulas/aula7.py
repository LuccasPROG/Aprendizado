import os
while True:
    try:
        nome = str(input('Digite seu Nome:'))
        horario = float(input('Digite seu horario agora:'))
        if horario >= 0 and horario <= 11:
            os.system('cls')
            print(f'ola, {nome} são {horario:.2f}, Bom Dia!')
            break
        elif horario >= 12 and horario <= 17:
            os.system('cls')
            print(f'ola, {nome} são {horario:.2f}, Bom Tarde!')
            break
        elif horario >= 18 and horario <= 23:
            os.system('cls')
            print(f'ola, {nome} são {horario:.2f}, Bom Noite!')
        else:
            print('Não conheço essa hora !')
            continue
    except(ValueError):
        print('Digite um Numero inteiro!')
        continue
print('>> Volte sempre <<')
