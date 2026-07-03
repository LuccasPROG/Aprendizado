# C:\Users\lucas\Documents\teste

import os

caminho = os.path.join('/Users', 'lucas', 'Documents', 'teste')


for pasta in os.listdir(caminho):
    caminho_completo_pasta = os.path.join(caminho, pasta)
    print(pasta)
    if not os.path.isdir(caminho_completo_pasta):
        continue

    for imagen in os.listdir(caminho_completo_pasta):
        print('    ',imagen)