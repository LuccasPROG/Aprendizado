import time
def verifica_imparoupar(numero):
    if numero % 2 == 0:
        return 'par'
    return 'impar'

def imparoupar():
    while True:
        numero = int(input('Digite um Numero(digite 0 para encerrar):'))
        resultado = verifica_imparoupar(numero)
        if numero == 0:
            break
        print(f'o numero {numero} é {resultado}')
def verificador_de_numeros(numero): 
    if numero > 0: 
        return 'Positivo'
    elif numero < 0: 
        return 'Negativo' 
    return 'Zero'

def positivos_negativos_zero():
    while True:
        Numero_digitado = int(input('Digite um Numero(digite 0 para encerrar): ')) 
        Resultado = verificador_de_numeros(Numero_digitado) 
        if Numero_digitado == 0 :
            break
        print(f'Seu numero {Numero_digitado} digitado e {Resultado}')

def numero_infinito():
    while True:
        numero = int(input('Digite um Numero (Digite "0" para encerrar): '))
        if numero == 0:
            print('Você encerrou o numero automatico')
            print('encerrando', end='')
            time.sleep(0.5)
            print('.', end='')
            time.sleep(0.5)
            print('.', end='')
            time.sleep(0.5)
            print('.', end='')
            time.sleep(0.5)
            break
while True:
    print('-='*20)
    print('Tabela da Escolha')
    print('-='*20)
    print('''
    1- Impar ou Par
    2- Positivo negativo ou zero
    3- Numero Infinito
    4- Sair
    ''')
    opcao = int(input('Digite uma Opção:'))

    if opcao == 1:
        imparoupar()
    elif opcao == 2:
        positivos_negativos_zero()
    elif opcao == 3:
        numero_infinito()
    elif opcao == 4:
            print('encerrando', end='')
            time.sleep(0.5)
            print('.', end='')
            time.sleep(0.5)
            print('.', end='')
            time.sleep(0.5)
            print('.', end='')
            time.sleep(0.5)
            break
    



