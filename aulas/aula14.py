from os import system
lista = []
while True:
    print('Selecione uma opção')
    listas = str(input('[1]inserir '
    '[2]apagar '
    '[3]listar:'))

    if listas == '1':
        system('cls')
        lista.append(input('Valor:'))
        print('Valor adicionado com sucesso!')
    elif listas == '2':
        try:
            system('cls')
            lista.pop(int(input('Digite um Valor para apagar:')))
            print('Valor apagado com sucesso!')
        except:
            system('cls')
            print('Valor não Encontrado!')
    elif listas == '3':
        if '' in lista:
            print('Não existe nada para ver!')
        else:
            system('cls')
            if len(lista) == 0:
                print('Não Existe nada para mostar!')
            else:
                print('-='*10)
                print('LISTA DESEJADA ')
                print('-='*10)
                for n, valor in enumerate(lista):
                    print(n, valor)
                print('-='*10)
    else:
        print('ERRO: Essa opção não existe!')
    try:
        resp = str(input('Deseja continuar?[S/N]:')).upper().strip()[0]
        if resp == 'N':
            break
    except:
        print('Digite somente o valor S ou N')
print('>> Volte Sempre <<')