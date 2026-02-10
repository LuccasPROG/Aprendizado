def criar_contador():
    numero = 0
    def interna():
        nonlocal numero
        numero += 1
        return numero
    return interna

contador1 = criar_contador()
contador2 = criar_contador()

print(contador1())
print(contador1())
print(contador1())
print(contador2())
print(contador2())
print(contador2())
print(contador2())