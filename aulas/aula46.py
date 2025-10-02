#Count  - itertools (Conta Infinity)

import itertools

conta = itertools.count(0,2)# iterador que conta infinitos no caso quase igual range() 
print('Count:')
for i in conta:
    if i > 100:
        break
    print(i)
print()
print('Range:')
for i in range(0,100,2):#Mesma coisa do count! acima ^
    print(i)
