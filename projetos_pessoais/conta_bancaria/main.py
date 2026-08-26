
class ContaBancaria:
    def __init__(self, numeroconta, nometitular, saldo) -> None:
        self.numeroconta = numeroconta
        self.nometitular = nometitular
        self.saldo = saldo

    def depositar(self, valor):
        if valor > 0 :
            self.saldo += valor
        else:
            print('ERROR: Deposito invalido!')

    def sacar(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
        else:
            print('ERROR: Valor inválido ou saldo insuficiente!')

    def transferir(self, contadestino, valor):
        if valor > 0 and valor <= self.saldo:
            self.sacar(valor)
            contadestino.depositar(valor)
        else:
            print('ERROR: Valor inválido ou saldo insuficiente!')

    def __repr__(self):
        classname = type(self).__name__
        classdict = self.__dict__
        classrepr = f'{classname}{classdict}'
        return classrepr

    def mostrar_dados(self):
        print(f'''
Conta: {self.numeroconta}
Nometitular: {self.nometitular}
Saldo: {self.saldo}''')
        print()

conta1 = ContaBancaria(123, 'Lucas', 100)
conta1.depositar(100)
conta1.sacar(50)
conta1.mostrar_dados()
conta2 = ContaBancaria(148, 'suelen', 2000)
conta2.transferir(conta1, 1000)
conta2.mostrar_dados()
conta1.mostrar_dados()
