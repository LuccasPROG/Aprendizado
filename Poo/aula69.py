maior = None
menor = None
soma = 0


for i in range(1, 11):
    numeros = int(input(f'Digite o {i}° Numero:'))

    soma += numeros
    if maior is None or numeros > maior:
        maior = numeros
    if menor is None or numeros < menor:
        menor = numeros
media = soma / 10
print(f'o Maior numero digitado é {maior}')
print(f'o Menor numero digitado é {menor}')
print(f'a media numero digitado é {media}')







# numeros = []

# for numero in range(1, 11):
#     pergunta = int(input(f'Digite o {numero}° Numero:'))
#     numeros.append(pergunta)


# print(f'o Maior numero digitado é {max(numeros)}')
# print(f'o Menor numero digitado é {min(numeros)}')
# print(f'a media numero digitado é {sum(numeros) / len(numeros)}')