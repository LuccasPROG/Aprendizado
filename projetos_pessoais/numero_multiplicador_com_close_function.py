def criar_multiplicador(multiplicador):
    def numero(numeros):
        print(f'{numeros * multiplicador}')
    return numero

numero_dobro = criar_multiplicador(2)
numero_triplo = criar_multiplicador(3)

numero_dobro(5)
numero_triplo(3)