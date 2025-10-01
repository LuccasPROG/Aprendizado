#Ordem de aplicação dos decoradores
def parametros_decorador(nome):
    def decorador(func):
        print('Decorador', nome)

        def sua_nova_funcao(*args, **kwargs):
            resultado = func(*args, **kwargs)
            final = f'{resultado} {nome}'
            return final
        return sua_nova_funcao
    return decorador

@parametros_decorador(nome='Primeiro')
def soma(x, y):
    return x + y

somando = soma(10, 5)
print(somando)