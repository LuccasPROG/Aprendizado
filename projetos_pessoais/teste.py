def criar_funcao(func):
    
    def interna(*args, **kwargs):
        for arg in args:
            e_string(args)

        resultado = func(*args, **kwargs)

        return resultado
    
    return interna


def inverte_string(string):
    return string[::-1]


def e_string(parametro):
    if not isinstance(parametro, str):
        raise TypeError('ERROR: Digite uma letra Não Número!')

inverte_string_checando_parametro = criar_funcao(inverte_string)

invertida = inverte_string_checando_parametro('123')
print(invertida)