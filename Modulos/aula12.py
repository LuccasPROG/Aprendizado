# os + shutil - Copiando arquivos com Python
# Vamos copiar arquivos de uma pasta para outra.
# Copiar -> shutil.copy
import os
import shutil

HOME = os.path.expanduser('~')
DOCUMENTS = os.path.join(HOME, "Documents")
PASTA_ORIGINAL = os.path.join(DOCUMENTS, 'teste')
NOVA_PASTA = os.path.join(DOCUMENTS, 'NOVA_PASTA')


os.makedirs(NOVA_PASTA, exist_ok=True)

for root, dirs, files, in os.walk(PASTA_ORIGINAL):
    for dir_ in dirs:
        caminho_novo_diretorio = os.path.join(root.replace(PASTA_ORIGINAL, NOVA_PASTA), dir_)
        print(caminho_novo_diretorio)
        os.makedirs(caminho_novo_diretorio, exist_ok=True)

    for file in files:
        caminho_arquivo = os.path.join(root, file)
        caminho_novo_arquivo = os.path.join(root.replace(PASTA_ORIGINAL, NOVA_PASTA), file)
        print(caminho_novo_arquivo)
        shutil.copy(caminho_arquivo, caminho_novo_arquivo)