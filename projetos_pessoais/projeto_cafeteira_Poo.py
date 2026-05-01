import os
class Items:
    def __init__(self, nome, preco, tipo):
        self.nome = nome
        self.preco = preco
        self.tipo = tipo
    

class Pedidos:
    def __init__(self):
        self.pedidos = []
        self.total = 0

class ItemPedido:
    def __init__(self, produto, quantidade):
        self.produto = produto
        self.quantidade = quantidade
        self.subtotal = produto.preco * quantidade


class Cafeteria:
    def __init__(self):

        self.pedido = Pedidos()

        self.comida = [
                Items('Croissant', 4.50, 'comida'),
                Items('Pão na chapa', 3.00, 'comida'),
                Items('Rosquinha', 3.50, 'comida'),
                Items('Pão de queijo', 5.00, 'comida'),
                Items('Coxinha', 6.00, 'comida'),
                Items('Empada', 5.50, 'comida'),
        ]
        self.bebida = [
                Items('Café expresso', 2.00, 'bebida'),
                Items('Cappuccino', 6.00, 'bebida'),
                Items('Chocolate quente', 5.50, 'bebida'),
                Items('Suco de laranja', 4.00, 'bebida'),
                Items('Refrigerante', 5.00, 'bebida'),
                Items('Água', 2.50, 'bebida'),
        ]

    def linha(self):
        print('-='* 20)

    def _Mostra_Menu(self):
            self.linha()
            print('             Cafeteria do Mana')
            self.linha()
            print('''
            1. Comida 
            2. Bebidas
            3. Sair''')

    def metodo_comida(self):
        os.system('cls')
        self.linha()
        print('             COMIDAS MANA')
        self.linha()

        for i, item in enumerate(self.comida, start=1):
            print(i, item.nome, item.preco)
        escolha = int(input('Digite sua Opção: '))
        if 1 <= escolha <= len(self.comida):
            produto = self.comida[escolha - 1]
            quantidade = int(input(f'Digite quantos {produto.nome} deseja: '))
            item_pedido = ItemPedido(produto, quantidade)
            self.pedido.pedidos.append(item_pedido)
            self.pedido.total += item_pedido.subtotal
            
    def metodo_bebida(self):
        os.system('cls')
        self.linha()
        print('             COMIDAS MANA')
        self.linha()

        for i, item in enumerate(self.bebida, start=1):
            print(i, item.nome, item.preco)
        escolha = int(input('Digite sua Opção: '))
        if 1 <= escolha <= len(self.bebida):
            produto = self.bebida[escolha - 1]
            quantidade = int(input(f'Digite quantos {produto.nome} deseja: '))
            item_pedido = ItemPedido(produto, quantidade)
            self.pedido.pedidos.append(item_pedido)
            self.pedido.total += item_pedido.subtotal

    def _iniciar(self):
        while True:
            self._Mostra_Menu()
            opcao = int(input('Sua Opção: '))

            if opcao == 1:
                self.metodo_comida()
            elif opcao == 2:
                self.metodo_bebida()
            elif opcao == 3:
                self.linha()
                print('Pedidos Total')
                self.linha()

                for i, item in enumerate(self.pedido.pedidos, start=1):
                    print(f'{i}.{item.produto.nome:<15} x{item.quantidade} = R${item.subtotal:.2f}')
                print(f'Total: R${self.pedido.total:.2f}')
                input('Digite enter Para Continuar: ')
                break



#INICIO
cafeteria = Cafeteria()
cafeteria._iniciar()