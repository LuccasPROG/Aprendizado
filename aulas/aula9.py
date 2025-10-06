try:
    while True:
        print('-='*10)
        print('     CALCULADORA')
        print('-='*10)
        n1 = int(input('Digite o Primeiro Valor:'))
        n2 = int(input('Digite o Segundo Valor:'))
        print('-='*10)
        print('|Calcular em :')
        print(f'''|Opção 1 = Somar
|Opção 2 = Subtrair
|Opção 3 = Multiplicar
|Opção 4 = Divisão
|Opção 5 = Sair ''')
        opcao = int(input('|Opção:'))
        print('-='*20)
        if opcao == 1:
            soma = n1 + n2
            print(f'A soma do numero {n1} + {n2} é igual a {soma}') 
            print('-='*20)
        elif opcao == 2:
            sub = n1 - n2
            print(f'A subtração do {n1} - {n2} é igual a {sub}')
            print('-='*20)
        elif opcao == 3:
            mult = n1 * n2
            print(f'A multiplicação do numero {n1} x {n2} é igual a {mult}')
            print('-='*20)
        elif opcao == 4:
            div = n1 / n2
            print(f'A Divisão do numero {n1} / {n2} é igual a {div:.2f}')
            print('-='*20)
        elif opcao == 5:
            break
        else:
            print('ERRO: Essa Opção não Existe, Tente novamente!')
except:
    print('ERRO: Digite um Numero Inteiro!')
finally:
    print('>>> Obrigado por usar a calculadora <<<')
    print()