#entender isso e bom
def criar_duplicador(multiplicador):
    def multiplica(numero):
        return numero * multiplicador
    return multiplica

dobro = criar_duplicador(2)
tripli = criar_duplicador(3)
quadriplicar = criar_duplicador (4)

print(dobro(5))
print(tripli(5))
print(quadriplicar(5))
# ===========================================================


# def duplica_numeros(num):
#     dobro = num * 2
#     triplo = num * 3
#     quadriplica = num * 4
#     return dobro,triplo,quadriplica

# valor = int(input('Digite um Numero:'))
# numeros = duplica_numeros(valor)
# print(f'O valor {valor} duplicado é {numeros[0]}, triplicados é {numeros[1]} quadriplicado é {numeros[2]}')