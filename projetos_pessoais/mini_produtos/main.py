class Produto:
    def __init__(self, nome, preco, quantidade) :
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
        

    def exibir_dados(self):
        print(f'''
nome: {self.nome}
Preço: {self.preco:.2f}
quantidade: {self.quantidade}
valor Total: {self.valor_total()}
''')

    def valor_total(self):
        total = 0
        total = self.preco * self.quantidade
        return total

n1 = Produto("arroz", 8, 30)
n1.exibir_dados()
