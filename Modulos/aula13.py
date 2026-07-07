# Vamos copiar arquivos de uma pasta para outra.
# Copiar -> shutil.copy
# Copiar Árvore recursivamente -> shutil.copytree
# Apagar Árvore recursivamente -> shutil.rmtree
# Apagar arquivos -> os.unlink
# Renomear/Mover -> shutil.move ou os.rename

import os
import shutil

HOME = os.path.expanduser('~')
DOCUMENTS = os.path.join(HOME, "Documents")
PASTA_ORIGINAL = os.path.join(DOCUMENTS, 'teste')
NOVA_PASTA = os.path.join(DOCUMENTS, 'NOVA_PASTA')

shutil.rmtree(NOVA_PASTA)

shutil.copytree(PASTA_ORIGINAL, NOVA_PASTA)
shutil.move(NOVA_PASTA, NOVA_PASTA + 'teste2')