class Carrinho:
    def __init__(self):
        self._produto = []

    
    def total(self):
        return sum([p.preco for p in self._produto])
    
    def listar_produtos(self):
        for produto in self._produto:
            print(produto.nome, produto.preco)

    def insetir_produtos(self, *produtos):
        for produto in produtos:
            self._produto.append(produto)

class Produto:
    def __init__(self, produto, preco):
        self.nome = produto
        self.preco = preco


carrinho = Carrinho()

p1, p2 = Produto('Caneta', 2.10), Produto( 'Chinelo', 30)

carrinho.insetir_produtos(p1, p2)
carrinho.listar_produtos()