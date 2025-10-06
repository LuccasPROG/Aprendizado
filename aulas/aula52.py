# Funções recursivas e recursividade
# - funções que podem se chamar de volta
# - úteis p/ dividir problemas grandes em partes menores
# Toda função recursiva deve ter:
# - Um problema que possa ser dividido em partes menores
# - Um caso recursivo que resolve o pequeno problema
# - Um caso base que para a recursão
#____________________________________________________________#
# def recursiva (inicio=0, fim=4):
# # função recursiva contar numeros ate o final
#     print(inicio, fim)
#     if inicio >= fim:
#         return fim
    
#     inicio += 1
#     return recursiva(inicio, fim)

# #Inicio: 

# print(recursiva(0,2000))
#____________________________________________________________#
#Funções Recursivas!
def factorial(n):
    if n <= 1:
        return 1
    
    return n * factorial(n -1)

# Inicio:
print(factorial(5))