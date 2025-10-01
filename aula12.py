
palavra_secreta = 'amor'
letra_acertadas = ''
tentativa = 0

import os
while True:
    letra_digitada = input('Digite uma letra:')
    tentativa += 1

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra.')
        continue
    
    if letra_digitada in palavra_secreta:
        letra_acertadas += letra_digitada


    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letra_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += ('*')
    print(f'Palavra formada: {palavra_formada}')
    if palavra_formada == palavra_secreta:
        os.system('cls')
        print('Você ganhou!')
        print(f'A palavra era : {palavra_secreta}')
        print(f'Você ganhou na tentativa {tentativa}x')
        letra_acertadas = ''
        tentativa = 0
        resp = ' '
        while resp not in 'SN':
            resp = input('Deseja Continuar? [S/N]:').upper().strip()[0]
            if resp not in 'SN':
                print('ERRO: Digite uma palavra entre S ou N')
                os.system('cls')
                continue
        if resp == 'N':
            os.system('cls')
            break
        else:
            continue
print('>> Obrigado por jogar >>')