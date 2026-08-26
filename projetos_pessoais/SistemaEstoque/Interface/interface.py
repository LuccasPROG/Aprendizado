import os
from database.Database import Banco_De_Dados 
from ProdutoRepository.ProdutoRepository1 import ProdutoRepository, Produto

class Interface:
    def _linha(self):
        print('-=' * 20)

    def _painel(self):
        self._linha()
        print('           SISTEMA DE ESTOQUE')
        self._linha()
        print(f'''
1 = Cadastro De produtos
2 = Visualizar Estoque
3 = Atualizar Produtos
4 = Deletar Produtos
5 = Sair
''')

class Main:
    def __init__(self):
        self._Interface = Interface()
        self.banco = Banco_De_Dados()
        self.repository = ProdutoRepository(self.banco)
        
    
    def _Inicio(self):
        while True:
            self._Interface._painel()

            opcao = int(input('Digite sua opção: '))

            if opcao == 1:
                name = input('Digite o Nome do produto: ')
                price = float(input('Digite o Preco do produto: '))
                amount = int(input('Digite a quantidade de produtos: '))
                code = int(input('Digite o codigo do produto : '))
                produtos = Produto(name, price, amount, code)
                self.repository.salvar(produtos)

            elif opcao == 2:
                p = self.repository.listar()
                os.system('cls')
                print('-='*20)
                print('          Estoque de Produtos')
                print('-='*20)
                for produto in (p):
                    print(f'|ID: {produto.id} | Nome: {produto.name} | Preço: {produto.price:.2f} | Quantidade: {produto.amount} | Codigo: {produto.code}|')
                input('Digite ENTER para Continuar ...')

            elif opcao == 3:
                id3 = int(input('Digite o id do Produto:'))
                name = input('Digite o novo Nome do produto: ')
                price = float(input('Digite o novo Preco do produto: '))
                amount = int(input('Digite a nova quantidade de produtos: '))
                code = int(input('Digite o novo codigo do produto: '))
                produto = Produto(
                    name=name,
                    price=price,
                    amount=amount,
                    code=code,
                    id=id3,
                )
                self.repository.update(produto)

            elif opcao == 4:
                p = self.repository.listar()
                os.system('cls')
                print('-='*20)
                print('          Estoque de Produtos')
                print('-='*20)
                for produto in (p):
                    print(f'|ID: {produto.id} | Nome: {produto.name} | Preço: {produto.price:.2f} | Quantidade: {produto.amount} | Codigo: {produto.code}|')
                input('Digite ENTER para Continuar ...')

                deleter= int(input('Digite o ID que Deseja deletar: '))
                self.repository.delete(deleter)
            elif opcao == 5:
                break