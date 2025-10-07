#poblema dos parâmetros mutáveis em funções Python
#não passar valores mutaveis como valores padrão em funções!
def adiciona_cliente(nome, lista=None):
    if lista is None:
        lista = []
    lista.append(nome)
    return lista

cliente1 = adiciona_cliente('Carlos')
cliente1 = adiciona_cliente('Maria', cliente1)
cliente1 = adiciona_cliente('Valentina', cliente1)
cliente2 = adiciona_cliente('Fernando')
cliente2 = adiciona_cliente('Maria José', cliente2)
cliente2 = adiciona_cliente('Felipe Neto', cliente2)

print(cliente1)
print(cliente2)