# a = 10
# b = 
# c = a / b
# print(c)
try:
    a = 10
    b = 0
    c = a / b
    print(c)

except(ZeroDivisionError):
    print('Você tentou dividizer por zeroo burro!')

except(NameError):
    print('tem valor faltando lerdo(a)!')

except(TypeError, IndexError ) as error: # criando uma variavel error que mostra o erroproposto
    print('TypeError + IndexError')
    print('MSG:', error)#variavel que mostra qual erro foi feito!
    print('Nome:', error.__class__.__name__)#Mostra qual o nome do erro!

except Exception:
    print('ERRO DESCONHECIDO ...')

print('CONTINUAR . . .')