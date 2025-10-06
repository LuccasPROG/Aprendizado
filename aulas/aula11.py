frase = 'O GATO ROEU A ROUPA DO REI DE ROMA, QUE O REI MATOU O RATO QUE PODERIA' \
' SE TORNAR UM QUARDA ROUPA FERIDO MATANDO O RATO JURADO DE MORTE'
qtd_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''
i = 0
while i < len(frase):
   letra = frase[i]
   if letra == ' ':
      i += 1
      continue
   qtd_apareceu_mais_vezes_atual = frase.count(letra)

   if qtd_apareceu_mais_vezes < qtd_apareceu_mais_vezes_atual:
      qtd_apareceu_mais_vezes = qtd_apareceu_mais_vezes_atual
      letra_apareceu_mais_vezes = letra
   i += 1

   print(f'A letra que apareceu mais vezes foi {letra_apareceu_mais_vezes} que apareceu {qtd_apareceu_mais_vezes}')