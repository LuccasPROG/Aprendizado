class ContaBancaria:
    def __init__(self, titular) -> None:
        self.titular = titular
        self.saldo = 0

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f'Sucess: you deposited {valor}')
        else:
            print('ERROR: Enter a Value greater than 0')

    def sacar(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            print(f'Success: You withdrew for {valor}')
        else:
            print(f'ERROR: you not withdrew for {valor}')

    def consultar_saldo(self):
        return self.saldo

conta1 = ContaBancaria('João')
conta1.consultar_saldo()
conta1.depositar(10)
conta1.consultar_saldo()
conta1.sacar(10)
conta1.consultar_saldo()

print(f'''
Nome: {conta1.titular } 
balance:{conta1.consultar_saldo()}''')



