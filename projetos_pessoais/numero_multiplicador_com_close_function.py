def criar_multiplicador(multiplicador):
    def interna(numero):
        print(f'{multiplicador * numero}')
    return interna

dobro = criar_multiplicador(int(input('Digite o numero multiplicador: ')))

dobro(int(input('Digite o numero que deseja multiplicar: ')))