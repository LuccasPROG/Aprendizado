# Dictionary e set comprehension

produtos = {
    'nome': 'Caneta Azul',
    'preco': 2.50,
    'categoria': 'Escritorio'
}

# for chave, valor in produtos.items():
#     print(chave, valor)

dc = {
    chave:valor.upper()
    if isinstance(valor, str) else valor #traduzindo se valor for str faça upper senão return valor
    for chave, valor in produtos.items()
    if chave != 'categoria' # filtra oq vc quer mostra vc que decide lucas
}
# print(dc)

# _____________________________________________
# SET

s1 = {i for i in range(10)}

print(s1)