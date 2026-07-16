# Comandos igual o Git ADD . adicionar coisas por 
# linha de comandos no terminal!
import sys

argumentos = sys.argv
qtd_argumentos = len(argumentos)

if qtd_argumentos <= 1:
    print('Você Não passou Argumentos')
else:
    try:
        print(f'VOcê Passou os argumentos {argumentos[1:]}')
        print(f'Faça alguma coisa com {argumentos[1]}')
        print(f'Faça outra coisa com {argumentos[2]}')
    except IndexError:
        print('Falta Algumentos')