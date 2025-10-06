'''
GERA UM CPF NOVO!
'''
from random import randint


nove_digitos_1 = '' #gera nove numeros e joga em nove_digitos_1
for numero in range(9):
    nove_digitos_1 += str(randint(0,9))


contador_regressivo_1 = 10# acha o primeiro numero
resultado_1 = 0
for digito in nove_digitos_1:
    resultado_1 += (int(digito) * contador_regressivo_1)
    contador_regressivo_1 -= 1
digito_1 = (resultado_1 * 10 % 11)
#verifica se o digito e menor ou igual a 9  else: digito vira 0
if digito_1 <= 9:
    digito_1 = digito_1
else:
    digito_1 = 0

dez_digitos_2 = nove_digitos_1 + (str(digito_1)) #acha o segundo numero!
contador_regressivo_2 = 11
resultado_2 = 0
for digito in dez_digitos_2:
    resultado_2 += (int(digito) * contador_regressivo_2)
    contador_regressivo_2 -= 1
digito_2 = (resultado_2 * 10) % 11 

if digito_2 <= 9:
    digito_2 = digito_2
else:
    digito_2 = 0

cpf_gerado_pelo_calculo = f'{nove_digitos_1}{digito_1}{digito_2}'

print(cpf_gerado_pelo_calculo)