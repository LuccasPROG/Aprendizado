def multiplicador(*args):
    total = 1
    for numero in args:
        total *= numero
    return total

total = []
while True:
    numero = int(input('Digite um Numero (ou digite 0 para sair):'))
    
    if numero == 0:
        break
    total.append(numero)

resultado = multiplicador(*total)
print(resultado)
