class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.enderecos = []

    def inserir_endereco(self, rua, numero):
        self.enderecos.append(Endereco(rua, numero))

    def mostrar(self):
        for casa in self.enderecos:
            print(casa.rua, casa.numero)


class Endereco:
    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero

cliente1 = Cliente('Maria')
cliente1.inserir_endereco('av brasil', 841651)
cliente1.inserir_endereco('av boa vista', 456789)
cliente1.mostrar()
