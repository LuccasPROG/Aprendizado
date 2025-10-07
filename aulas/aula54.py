# Criando arquivos com Python + Context Manager with
# Usamos a função open para abrir
# um arquivo em Python (ele pode ou não existir)
# Modos:
# r (leitura), w (escrita), x (para criação)
# a (escreve ao final), b (binário)
# t (modo texto), + (leitura e escrita)
# Context manager - with (abre e fecha)
# Métodos úteis
# write, read (escrever e ler)
# writelines (escrever várias linhas)
# seek (move o cursor)
# readline (ler linha)
# readlines (ler linhas)
# Vamos falar mais sobre o módulo os, mas:
# os.remove ou unlink - apaga o arquivo
# os.rename - troca o nome ou move o arquivo
# Vamos falar mais sobre o módulo json, mas:
# json.dump = Gera um arquivo json
# json.load

caminho_arquivo = 'C:\\Users\\lucas\\OneDrive\\Área de Trabalho\\TI\\Python\\Cursoudemy\\'
caminho_arquivo += 'aula55.txt'

# arquivo = open(caminho_arquivo, 'w')
#um exemplo de abrir arquivo
# arquivo.close()


#with ele abre e fecha o arquivo sosinho
# with open(caminho_arquivo, 'w+') as arquivo:# w+ ele le e pode escrever junto mais o w ele apaga oq esta dentro da pasta
#     arquivo.write('Linha 1\n')#escrevendo dentro do arquivo txt
#     arquivo.write('Linha 1\n')#escrevendo dentro do arquivo txt
#     arquivo.writelines(#escreve varias linhas mais o write serve tbm !
#         ('linha 3\n','linha 4\n')
#     )
#     arquivo.seek(0, 0) # move o cursor para cima colocar antes de ler o arquivo
#     print(arquivo.read())#Lendo o arquivo linha por linha
#     print('lendo')
#     arquivo.seek(0, 0) # move o cursor para cima colocar antes de ler o arquivo
#     print(arquivo.readline(), end='')#tipo o next do interavel obs(usar end apara tirar os espaços ou usar o strip() )
#     print(arquivo.readline().strip())#tipo o next do interavel obs(usar end apara tirar os espaços ou usar o strip() )
#     print(arquivo.readline().strip())#tipo o next do interavel obs(usar end apara tirar os espaços ou usar o strip() )
#     print(arquivo.readline().strip())#tipo o next do interavel obs(usar end apara tirar os espaços ou usar o strip() )
#     print('Readlines')
#     arquivo.seek(0, 0) # move o cursor para cima colocar antes de ler o arquivo
#     for linha in arquivo.readlines():
#         print(linha.strip())


# print('#'*30)


# with open(caminho_arquivo, 'r') as arquivo:
#     print(arquivo.read())#Lendo o arquivo
import os
with open(caminho_arquivo, 'a+', encoding='utf8') as arquivo:# a+ ele nao apaga ele continua na ultima linha
    arquivo.write('Linha 1\n')#escrevendo dentro do arquivo txt
    arquivo.write('Linha 1\n')#escrevendo dentro do arquivo txt
    arquivo.writelines(#escreve varias linhas mais o write serve tbm !
        ('linha 3\n','linha 4\n')
    )
# importa os e os dois remove e unlink removem um arquivo txt
# os.remove(caminho_arquivo) 
# os.unlink(caminho_arquivo)

#importa os ele renomeia o arquivo ou melhor move para um novo nome!
# os.rename(caminho_arquivo, 'aula54-2.txt')