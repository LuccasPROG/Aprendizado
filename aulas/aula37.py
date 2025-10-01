# print(123)
# raise SyntaxError('\033[31mVocê errou a conta !!!')#raise  cria seu proprio erro no caso ele edita o erro
# print(456)


#________________________________________________________________________
# raise - lançando exceções (erros)
# https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions

def nao_zero(b):
    if b == 0:
        raise ZeroDivisionError('Você esta tentando dividir por zero burro!')
    return True

def deve_ser_int_ou_float(n):
    if not isinstance(n, (float, int)):
        raise TypeError(f'"{n}" deve ser um numero int ou float!!')
    return True

def divide(n, d):
    nao_zero(d)
    deve_ser_int_ou_float(n)
    deve_ser_int_ou_float(d)
    return n / d

#INICIO:
divisão = divide(8,0)
print(divisão)