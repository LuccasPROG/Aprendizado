#Funções Decoradoras em geral ou Decorador

def criar_funcao(func): #<- Função decoradora
    def interna(*args, **kwargs):
        print('Decorando as string')
        for arg in args:
            e_string(arg)
        resultado = func(*args, **kwargs)
        print(F'as String decorada foi {resultado}')
        print('Ok, ja decorei')
        return resultado
    return interna

def e_string(param):
    if not isinstance(param, str):
        raise TypeError('O parametro deve ser uma string !')
    
@criar_funcao
def nome_invertido(string):
    return string[::-1]

#INICIO
invertida = nome_invertido('sacul')
print(invertida)