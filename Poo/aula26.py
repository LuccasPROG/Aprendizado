
# Context Manager no Python
from contextlib import contextmanager



@contextmanager
def my_open(caminho_arquivo, modo):
    try:
        print('Abrindo arquivo')
        arquivo = open(caminho_arquivo, modo, encoding='utf8')
        yield arquivo
    except Exception as e:
        print('Ocorreu erro', e)    
    finally:
        print("fechando arquivo")


with my_open('aula26.txt', 'w',) as arquivo:
    arquivo.write('linha 1  \n')
    arquivo.write('linha 2  \n', 123)
    arquivo.write('linha 3  \n')
    print('WITH', arquivo)