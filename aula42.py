# Decoradores com parametros!

def fabrica_de_decoradores(a=None,b=None,c=None):# decoradores com parametros
    def fabrica_de_funcoes(func): # cria decoradores
        print('Decoradora 1')
        def aninhada(*args, **kwargs):
            print('Aninhada')
            print(f'Parametros do decorador {a} {b} {c}')
            resultado = func(*args, **kwargs)
            return resultado
        return aninhada
    return fabrica_de_funcoes

@fabrica_de_decoradores(1,2,3)
def soma(x, y):
    return x + y

#INICIO:
multiplica = lambda x, y: x * y # cria uma função que multiplica em lambda
decorador = fabrica_de_decoradores()

multiplicado = multiplica(5, 10)
somando = soma(5, 10)
print(somando)
print(multiplicado)