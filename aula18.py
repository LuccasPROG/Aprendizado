#exercicio criar uma função que retorne um valores em multiplicação!

def multiplicacao(*num):
    soma = 1
    for numero in num:
        soma *= numero
    return soma

#Inicio
multi = multiplicacao(3,3,2,4,6,2,3)
print(f'A multiplicação dos números digitados é {multi}')
print()