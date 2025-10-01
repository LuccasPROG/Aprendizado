#isintace - serve para saber se objeto é de determindado tipo

lista = [
    'a', 1, 1.1, True, [0, 1, 2], (1, 2),
    {0, 1}, {'nome':'lucas'}
]

for item in lista:

    if(isinstance(item, set)):
        print('SET')
        item.add(6)
        item.add(8)
        item.add(1)
        print(item, isinstance(item, set))

    elif(isinstance(item, str)):
        print('STR')
        print(item.upper())

    elif (isinstance(item, (int, float))):
        print('NUM')
        print(f'{item} x {item} = {item * 2}')
    else:
        print('OUTRO')
        print(item)