# # PyPDF2 para manipular arquivos PDF (Instalação)
# PyPDF2 é uma biblioteca de manipulação de arquivos PDF feita em Python puro,
# gratuita e de código aberto. Ela é capaz de ler, manipular, escrever e unir
# dados de arquivos PDF, assim como adicionar anotações, transformar páginas,
# extrair texto e imagens, manipular metadados, e mais.
# A documentação contém todas as informações necessárias para usar PyPDF2.
# Link: https://pypdf2.readthedocs.io/en/3.0.0/
# Ative seu ambiente virtual
# pip install pypdf2

from pathlib import Path

from PyPDF2 import PdfReader

PASTA_RAIZ = Path(__file__).parent
PASTA_ORIGIN = PASTA_RAIZ / 'paginasorigin'
PASTA_NOVA = PASTA_RAIZ / 'arquivos_novos'

RELATORIO_BACEn = PASTA_ORIGIN / 'R20260717.pdf'
PASTA_NOVA.mkdir(exist_ok=True)
reader = PdfReader(RELATORIO_BACEn)

# print(len(reader.pages)) # ve quantas paginas tem no pdf
# for page in reader.pages: #olha o pdf
#     print(page)

# print(page0.extract_text()) Extrai Texto

page0 = reader.pages[0]
print(len(page0.images)) 
