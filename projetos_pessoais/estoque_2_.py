import os
import time
import json

class Estoque:
    def __init__(self):
        self.estoque = []
class CriarJson:
    @staticmethod
    def salvar(estoque):
        with open('estoque.json', 'w') as arquivo:
            json.dump(estoque.estoque, arquivo, ensure_ascii=False, indent=4)
    
    @staticmethod
    def carregar(estoque):
        try:
            with open('estoque.json', 'r') as arquivo:
                estoque.estoque = json.load(arquivo)
        except FileNotFoundError:
            estoque.estoque = []

class Verifica_Produtos:
    def __init__(self, nome, preco, quantidade, codigo, estoque):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
        self.codigo = codigo
        self.estoque = estoque

    #VALIDAÇÂO DE PRODUTOS
    def cadastro_de_produtos(self):
        codigo_existe = False # validação se o codigo ta duplicado
        produto = {
            'nome':self.nome,
            'preco':self.preco,
            'quantidade':self.quantidade,
            'codigo': self.codigo
        }
        for produto_existente in self.estoque.estoque:
            if produto_existente['codigo'] == self.codigo:
                codigo_existe = True
                break
        
        if codigo_existe: # esse if informa se o codigo ja exister o error!
            print('\033[1;31mERROR❌: Esse codigo já existe\033[m')
            time.sleep(1)
            print('\033[1;31mERROR❌: Não foi possivel fazer o cadastro!\033[m')
            time.sleep(1)
            input('Aperte ENTER para continuar ...')

        else:
            time.sleep(1)
            print('\033[1;32mCadastro feito com Sucesso!✅\033[m')
            time.sleep(1)
            self.estoque.estoque.append(produto)
            input('Aperte ENTER para continuar ...')
            CriarJson.salvar(self.estoque)

            os.system('cls')

class Produtos:
    def __init__(self):
        self.estoque = Estoque()
        CriarJson.carregar(self.estoque)
    def _linha(self):
         print('-=' * 20)

    def _menu(self):
        self._linha()
        print('           Sistema de Estoque')
        self._linha()

        print('''1. Cadastrar Produtos
2. Calcular o Total de Produtos em Estoque
3. Mostrar Produtos estoque
4. Sair''')
        

    def _iniciar(self):
        while True:
            try:
                self._menu()
                opcao = int(input('Digite sua Opção:'))
            except   ValueError:
                print('\033[1;31mError❌: Você digitou um numero invalido!\033[m')
                continue
            except:
                print('\033[1;31mError❌: Erro não cadastrado!\033[m')
            

            if opcao == 1:
                nome = input('Digite o nome do produto: ')
                preco = float(input('Digite o Preço do produto: '))
                while True:
                    while preco < 0:
                        print('\033[1;31mError❌: Você digitou um preço negativo!\033[m')
                        preco = float(input('Digite o Preço do produto: '))
                        time.sleep(1)

                    quantidade = int(input('Digite a quantidade de produtos: '))
                    while quantidade < 0 :
                        print('\033[1;31mError❌: Você digitou uma quantidade negativa!\033[m')
                        quantidade = int(input('Digite a quantidade de produtos: '))
                        time.sleep(1)
                        
                    codigo = int(input('Digite o codigo do produto: '))

                    obg =Verifica_Produtos(nome, preco, quantidade, codigo, self.estoque)
                    obg.cadastro_de_produtos()
                    break

            elif opcao == 2:
                total = 0
                for produto in self.estoque.estoque:
                    total += produto['quantidade']
                print(f'Total de Produto no estoque: {total}')
                input('Aperte ENTER para continuar ...')
                os.system('cls')    

            elif opcao == 3:
                self._linha()
                print('                 Estoque')
                self._linha()
                
                lista_de_estoque = CriarJson.carregar(self.estoque)

                for i, produto in enumerate(self.estoque.estoque):
                    print(f"{i + 1}) Nome: {produto['nome']}, Preço: {produto['preco']:.2f}, Quantidade: {produto['quantidade']}, Codigo: {produto['codigo']}.")
                    time.sleep(1)
                input('Aperte ENTER para continuar ...')
                os.system('cls')
                
            elif opcao == 4:
                os.system('cls')
                print('Encerrando',end='')
                time.sleep(1)
                print('.',end='')
                time.sleep(1)
                print('.')
                
                print('Volte sempre!👌')
                break

#Inicio
produto = Produtos()
produto._iniciar()