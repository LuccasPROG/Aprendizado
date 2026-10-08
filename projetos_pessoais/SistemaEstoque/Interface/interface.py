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
            try:
                opcao = int(input('Digite sua opção: '))
            except ValueError:
                    print('ERROR: Você digitou letras')
                    continue

            if opcao == 1:
                try:
                    name = input('Digite o Nome do produto: ').strip()
                    while name == '':
                        print('Error: Nome Vazio!!!')
                        name = input('Digite o Nome do produto: ').strip()
                        
                    price = float(input('Digite o Preco do produto: '))
                    while price < 0:
                        print('ERROR: Valor menor que 0')
                        price = float(input('Digite o Preco do produto: '))
                        
                    amount = int(input('Digite a quantidade de produtos: '))
                    while amount < 0:
                        print('ERROR: Valor menor que 0')
                        amount = int(input('Digite a quantidade de produtos: '))
                        
                    code = int(input('Digite o codigo do produto : '))
                    verificado = self.repository.verifica_codigo(code)
                    while verificado != None:
                        print('ERROR: Esse codigo já existe!')
                        code = int(input('Digite outro codigo do produto : '))
                        verificado = self.repository.verifica_codigo(code)
                    produtos = Produto(
                        name,
                        price,
                        amount,
                        code,
                        )
                    self.repository.salvar(produtos)
                except ValueError:
                    print('ERROR: Você digitou letras')
                    continue

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
                p = self.repository.listar()
                os.system('cls')
                print('-='*20)
                print('          Estoque de Produtos')
                print('-='*20)
                for produto in (p):
                    print(f'|ID: {produto.id} | Nome: {produto.name} | Preço: {produto.price:.2f} | Quantidade: {produto.amount} | Codigo: {produto.code}|')
                input('Digite ENTER para Continuar ...')

                try:
                    if not p:
                        print('ERROR: Não Existe nenhum dado para atualizar!')
                        continue
                    encontrado = False
                    id3 = int(input('Digite o id do Produto:'))

                    while encontrado == False:
                        for idss in p:
                            if id3 == idss.id:
                                encontrado = True
                        if encontrado == False:
                            print('ERROR: Esse ID não existe')
                            id3 = int(input('Digite um id existente do Produto:'))

                    name = input('Digite o novo Nome do produto: ').strip()
                    while name == '':
                        print('Error: Nome Vazio!!!')
                        name = input('Digite o novo Nome do produto: ').strip()
                    price = float(input('Digite o novo Preco do produto: '))
                    while price < 0 :
                        print('ERROR: Valor menor que 0')
                        price = float(input('Digite o novo Preco do produto: '))
                    amount = int(input('Digite a nova quantidade de produtos: '))
                    while amount < 0:
                        print('ERROR: Valor menor que 0')
                        amount = int(input('Digite a nova quantidade de produtos: '))
                    code = int(input('Digite o novo codigo do produto: '))
                    verificado = self.repository.verifica_codigo(code)
                    while verificado != None and  verificado[0] != id3:
                        print('ERROR: Esse codigo já existe!')
                        code = int(input('Digite outro codigo do produto : '))
                        verificado = self.repository.verifica_codigo(code)
                except ValueError:
                    print('ERROR: Você digitou letras')
                    continue

                produto = Produto(
                    name=name,
                    price=price,
                    amount=amount,
                    code=code,
                    id=id3,
                )
                self.repository.update(produto)

            elif opcao == 4:
                try:
                    p = self.repository.listar()
                    os.system('cls')
                    print('-='*20)
                    print('          Estoque de Produtos')
                    print('-='*20)
                    for produto in (p):
                        print(f'|ID: {produto.id} | Nome: {produto.name} | Preço: {produto.price:.2f} | Quantidade: {produto.amount} | Codigo: {produto.code}|')
                    input('Digite ENTER para Continuar ...')

                    if not p:
                        print('ERROR: não existe nenhum dado para deletar!')
                        continue
                    encontrado1 = False
                    deleter= int(input('Digite o ID que Deseja deletar: '))
                    while encontrado1 == False:
                            for idss in p:
                                if deleter == idss.id:
                                    encontrado1 = True
                            if encontrado1 == False:
                                print('ERROR: Esse ID não existe')
                                deleter= int(input('Digite o ID que Deseja deletar: '))
                    self.repository.delete(deleter)
                except ValueError:
                    print('ERROR: Digite somente Numeros!')
                    continue

            elif opcao == 5:
                break