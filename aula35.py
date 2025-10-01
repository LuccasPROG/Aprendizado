def gem():
    yield 1
    yield 2
    yield 3
    yield 4

def gem1():
    yield from gem()# Continua oq esta escrito na função gem()!!!!!
    yield 5
    yield 6
    yield 7
    yield 8
    yield 9
    yield 10
    print('Fim!')

num = gem1()

for i in num:
    print(f'{i}', end=' -> ')