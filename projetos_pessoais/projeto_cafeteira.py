
def linha ():
    print('-='*10)

comida =[{'nome':'Croissant', 'preco': 4.50},
         {'nome':'Pão', 'preco': 0.50},
         {'nome': 'Rosquinha', 'preco': 3.50}]

bebida =[{'nome':'Cafe', 'preco': 2.00},
          {'nome':'suco', 'preco': 3.00},
          {'nome':'refrigerante', 'preco': 5.00}]

pedidos = []
total = 0
while True:
    linha()
    print('Cafeteria do Mana')
    linha()
    print('''    1. Comida 
    2. Bebidas
    3. Sair''')
    opcao = int(input('Sua Opção: '))

    if opcao == 1:
        linha()
        print('Comidas')
        linha()
        for i, item in enumerate(comida, start=1):
            print(f'{i}.{item["nome"]:<15}   R${item["preco"]:>6.2f}')
        escolha  = int(input('Opção:'))
        if 1 <= escolha <= len(comida):
            quantidade = (int(input('Digite a Quantidade:')))
            produto = comida[escolha - 1]
            subtotal = produto['preco'] * quantidade
            pedidos.append({
                'nome':produto['nome'],
                'tipo':'comida',
                'quantidade':quantidade,
                'subtotal': subtotal
            })
            total += subtotal
            print(f'Pedido adicionado! subtotal: {subtotal:.2f}')

    elif opcao == 2:
        linha()
        print('Bebidas')
        linha()
        for i, item in enumerate(bebida,start=1):
            print(f'{i}. {item["nome"]:<15}    R${item["preco"]:<6.2f}')
        escolha = int(input('Opção:'))
        if 1 <= escolha <= len(bebida):
            quantidade = int(input('Quantidade:'))
            produto = bebida[escolha - 1]
            subtotal = produto['preco'] * quantidade
            pedidos.append({
                'nome' :produto['nome'],
                'tipo' : 'bebida',
                'quantidade': quantidade,
                'subtotal': subtotal
                }         
            )
            total += subtotal
            print(f'Pedido Adicionado! Subtotal:{subtotal:2f}')

    elif opcao == 3:
        linha()
        print('Pedidos Total')
        linha()
        for i, item in enumerate(pedidos,start=1):
            print(f'{i}.{item["nome"]:<15} Tipo:{item["tipo"]}')
        print(f'Total da Compra: {total}')
        break