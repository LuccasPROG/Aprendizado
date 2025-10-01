def executa(funcao, *args): # Função executa algo
    return funcao(*args)

def soma(x=0, y=0): #Função ela soma 2 valores!
    return x + y

def cria_multiplicador(multiplicador): #Multiplica valores
    def multiplica(numero):
        return numero * multiplicador
    return multiplica

# multiplicação = cria_multiplicador(2)

#exemplos de LAMBDA !
duplica = executa(
    lambda m: lambda n: n * m, #Função lambda que duplica um valor
    2 
)

print(duplica(2))

print(
    executa(
        lambda x, y: x + y, #Igual a função soma
        2, 3
        )
)
