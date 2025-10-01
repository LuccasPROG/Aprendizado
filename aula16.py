def funcao(x, y, z=None):
    if z is not None:
        print(f'{x=} {y=} {z=}| A + B + z = {x + y + z}')
    else:
        print(f'{x=} {y=} | A + B = {x + y}')


funcao(4,2)
funcao(4,2,)
funcao(4,2, 2)
funcao(z=2,x=8,y=10)

'''def funcao(a, b):
    print(f'{a=} {b=} | A + B = {a + b}')


n1 = int(input('Digite um Numero:'))
n2 = int(input('Digite outro Numero:'))
funcao(n1, n2)'''