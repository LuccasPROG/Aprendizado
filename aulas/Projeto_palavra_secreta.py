import os
import random
palavras_secreta = ['amor', 'carro', 'ovo', 'biscoito']
palavra_acertada = ''
palavras_erradas = ''
tentativa = 0
nome_da_palavra_secreta = random.choice(palavras_secreta)

def verificando_palavra_certa(letra, palavra_secreta):
    if letra in palavra_secreta:
        return letra
    return ''

def verificando_palavra_secreta(palavra_secreta, palavra_acertada):
     palavra_formada = ''
     for letra_secreta in palavra_secreta:
        if letra_secreta in palavra_acertada:
            palavra_formada += letra_secreta
        else:
             palavra_formada += "*"
     return palavra_formada



#INICIO
while True:
    letra = input('Digite uma Letra:').lower()
    tentativa += 1

    if letra in palavra_acertada or letra in palavras_erradas :
        print('Você ja digitou essa letra!')
        continue

    if len(letra) > 1:
        print('Error: Digite so uma letra')
        continue

    if letra in nome_da_palavra_secreta:
        if letra not in palavra_acertada:
            palavra_acertada += verificando_palavra_certa(letra, nome_da_palavra_secreta)
    else:
        if letra not in palavras_erradas:
            palavras_erradas += letra
    palavra_formada = verificando_palavra_secreta (nome_da_palavra_secreta, palavra_acertada)

    print(f'Palavra Formada:{palavra_formada}')

    if palavra_formada == nome_da_palavra_secreta:
        os.system('cls')
        print(f'Você Ganhou! na Tentativa {tentativa}x')
        print(f'As palavras erradas Digitadas foram: {palavras_erradas}')
        print('-=-'*10)
        resp = ' '
        while resp not in 'SN':
            resp = str(input('Deseja Continuar [S/N]')).upper().strip()
            if resp not in 'SN':
                print('Error: Digite uma S ou N !!')
        if resp == 'N':
            break

    if tentativa > 9:
        os.system('cls')
        print(f'Você perdeu por exeder o limite de tentativas {tentativa}x')
        print(f'A palavra certa era {nome_da_palavra_secreta}')
        break
print('Volte Sempre !!')