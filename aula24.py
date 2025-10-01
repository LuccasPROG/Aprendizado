# s1 = {1,2,3,4} #cria um SET
# s1.add('Lucas') # Adiciona  

# s1.update(('Carlos',1,2,3,4)) #Adiciona tbm Update

# s1.discard('Carlos')#remove algo dentro do SET

# s1.discard(4)

# # s1.clear()# apaga um SET

# # print(s1)

# s1 = {1,2,3}
# s2 = {2,3,4}

# s3 = s1 | s2 #União !

# s3 = s1 & s2 #Mostra oq esta presente em ambos !

# s3 = s1 - s2 #Mostra oq esta somente na esquerda no caso s1 ai

# s3 = s1 ^ s2 #Mostra oq tem somente em ambos não nessecita de lado
# print(s3)
letras = set()
while True:
    letra = input('Digite a palavra: ')
    letras.add(letra.lower())

    if 'best' in letras:
        print('Acertou a palavra')
        break

# Outro exeplo !
# palavra = set()
# for i in range(0,5):
#     nome = int(input('Digite um numero:'))
#     palavra.add(nome)
# print(palavra)