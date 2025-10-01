def parouinpar(n=0):
    int(n)
    if n % 2 == 0:
        par = 'PAR'
        return par
    else:
        impar = 'IMPAR'
        return impar


#INICIO
try:
    num = int(input('Digite um número:'))
    par_ou_impar = parouinpar(num)
    print(f'O Numero Digitado é {par_ou_impar}')
except ValueError:
    print('ERRO: Digite um número inteiro!')