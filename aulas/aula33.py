#ITERADOR Abaixo!!

# iterator = 'eu', 'tenho', '__iter__'
# iterador = iter(iterator)
# print(next(iterador))
# print(next(iterador))
# print(next(iterador))
#______________________________________________________
#Generator expression basicamente uma função que sabe pausar !
import sys
iterator = ['eu', 'tenho', '__iter__']
iterador = iter(iterator)
lista = [n for n in range(1000)]
generator = (n for n in range(1001))

print(sys.getsizeof(lista)) #verifica a peso na lista
print(sys.getsizeof(generator))#verifica a peso no gerador

for n in generator:
    print(n)