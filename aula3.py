while True:
    try:
            primeiro = int(input('Digite um valor:'))
            segundo = int(input('Digite outro valor:'))

            if primeiro > segundo:
                print(f'O valor {primeiro} é maior que valor {segundo}')
                break
            elif primeiro == segundo:
                print(f'O valor {primeiro} é igual a valor {segundo}')
                break
            else:
                print(f'O valor {segundo} é maior que o valor {primeiro}')
                break
    except:
        print('Erro: Você presisa Digitar um Numero!!!')
        continue
        
print('>>> Volte Sempre <<<')