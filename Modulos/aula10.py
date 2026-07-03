#  os.walk para navegar de caminhos de forma recursiva
# # os.walk é uma função que permite percorrer uma estrutura de diretórios de
# # maneira recursiva. Ela gera uma sequência de tuplas, onde cada tupla possui
# # três elementos: o diretório atual (root), uma lista de subdiretórios (dirs)
# # e uma lista dos arquivos do diretório atual (files).

import os
from itertools import count

caminho = os.path.join('/Users', 'lucas', 'Documents', 'teste')
counter = count()

for root, dirs, files in os.walk(caminho):
    the_conter = next(counter)
    print(the_conter, 'pasta atual', root)

    for dir_ in dirs:
        print('    ', the_conter, 'Dir:', dir_)

    for file_ in files:
        caminho_completo_arquivo = os.path.join(root, file_)
        print('    ', the_conter, 'files:', caminho_completo_arquivo)