#x, y, *resto =  1, 2, 3, 4, 5, 6, 7, 8, 9, 10
#print(x, y, resto)
from time import sleep
def soma(*num):
    soma = 0
    for numero in num :
        soma += numero
    return soma


#Inicio
numeros = soma(1,2,4,5,6,8,3,9,7)
num = 1,2,4,5,6,8,3,9,7
print(sum(num))
print(f'A soma dos Numeros é {numeros}')