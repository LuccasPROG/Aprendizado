# # exercicios = Adiando funções(minha forma é mais direta)
# def soma(x):
#     def soma_segundo_valor(y):
#         return x + y
#     return soma_segundo_valor


# def multiplica(x):
#     def multiplica_segundo_valor(y):
#         return x * y
#     return multiplica_segundo_valor


# def executa(funcao, *args):
#     return funcao(*args)


# soma_com_cinco = executa(soma, 5)
# multiplica_por_dez = executa(multiplica, 10)



# print(soma_com_cinco(5))
# print(multiplica_por_dez(10))

# exercicios = Adiando funções (Forma do Professor e mais Generica)
def soma(x, y):
    return x + y


def multiplica(x, y):
    return x * y


def executa(funcao, x):
    def interna(y):
        return funcao(x, y)
    return interna


soma_com_cinco = executa(soma, 5)
multiplica_por_dez = executa(multiplica, 10)



print(soma_com_cinco(10))
print(multiplica_por_dez(5))