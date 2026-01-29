import os
print('====================')
print('Jogo do Par ou Impar')
print('====================')
while True:
    try:
        numero1 = int(input('Digite um Numero:'))
        if numero1 % 2 == 0:
            os.system('cls')
            print('============================')            
            print(f'O numero {numero1} é PAR')
            print('============================')    
            break
        else:
            os.system('cls')
            print('============================')    
            print(f'O numero {numero1} é IMPAR')
            print('============================')    
            break
    except ValueError:
        os.system('cls')
        print('Digite um Numero Inteiro!')
        continue
print('Volte Sempre!')