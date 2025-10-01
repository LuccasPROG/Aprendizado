lista = [
        {'NOME': 'GABRIEL', 'SOBRENOME' : 'SILVA'},
        {'NOME': 'JÕAO', 'SOBRENOME':'ALMEIDA'},
        {'NOME': 'CARLOS', 'SOBRENOME': 'GUSTAVO'},
        {'NOME': 'LUCAS', 'SOBRENOME': 'EVELINTON'},
        {'NOME': 'VALENTINA', 'SOBRENOME': 'FERREIRA'},
        {'NOME': 'Suelen', 'SOBRENOME': 'FERREIRA'},
        {'NOME': 'EDNA', 'SOBRENOME': 'EVELLYN'},
        {'NOME': 'EDSON', 'SOBRENOME': 'DANTAS'},
]
#FUNÇÃO LAMBDA
def exibir(dicionario): #Função exibi valores
    for lista in dicionario:
        print(lista)
    print()

nome = sorted(lista, key=lambda item: item['NOME']) #Função lambda deixa em ordem o dicionario NOME
sobrenome = sorted(lista, key=lambda item: item['SOBRENOME']) #Função lambda deixa em ordem o dicionario SOBRENOME

exibir(nome) #Em ordem exibir em ordem alfabetica o NOMES
exibir(sobrenome) #Em ordem exibir em ordem alfabetica o SOBRENOME


    #Formato em Função:

# def ordena(item):
#     return item['NOME']

# lista.sort(key=ordena)
# for item in lista:
#     print(item)