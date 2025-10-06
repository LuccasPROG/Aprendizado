#Função filter ele filtra alguma coisa como demostra abaixo que mostra somente coisas acima de algo escolhido por lucas assim
#FIltrando uma lista ! 


produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

# novos_produtos = [ 
#     p for p in produtos 
#     if p['preco'] > 10
# ]
novo_produto = filter(# na primeira parte passa uma função pode ser tbm lambda e segundo passa o argumento !
    lambda p: p['preco'] > 100,
    produtos
)

for i in novo_produto:
    print(i)
print()

for i in produtos:
    print(i)
print()