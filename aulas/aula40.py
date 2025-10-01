#Variáveis livres + nonlocal(local, globas)

def concatenar(string_inicial):
    valor_final = string_inicial

    def interna(valor_a_concatenar=''):
        nonlocal valor_final
        valor_final += valor_a_concatenar
        return valor_final

    return interna


#Inicio
silabas = concatenar('a')
print(silabas(''))
print(silabas('b'))
print(silabas('c'))
print(silabas('d'))
final = silabas()
print('-- Valor Final --')
print(final)