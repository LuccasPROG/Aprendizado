# Exercício - Lista de tarefas com desfazer e refazer
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']
import os
import json
def ler (tarefas, caminho_arquivo):
    dados = []
    try:
        with open(caminho_arquivo, 'r', encoding='utf8') as arquivo:
            dados = json.load(arquivo)
    except FileNotFoundError:
        print('Esse arquivo não existe')
        salvar(tarefas, caminho_arquivo)
    return dados

def salvar(tarefas, caminho_arquivo):
        dados = tarefas
        with open(caminho_arquivo, 'w', encoding='utf8') as arquivo:
            dados = json.dump(
                tarefas,
                arquivo,
                indent=2)
        return dados

CAMINHO_ARQUIVO = 'aula57.json'
tarefas = ler([], CAMINHO_ARQUIVO)
refazer_tarefas = []

while True:
    print('Comandos : listar, desfazer, refazer, sair, clear')
    comando = str(input('Digite uma Tarefa ou comando: ')).strip()

    if comando == 'clear':
        os.system('cls')

    elif comando == 'listar':
        print('TAREFAS:')
        for tarefa in tarefas:
            print(tarefa)

    elif comando == 'desfazer':
        if tarefas:
            apagado = tarefas.pop()
            refazer_tarefas.append(apagado)
            print('TAREFAS:')
            for tarefa in tarefas:
                print(tarefa)
            salvar(tarefas, CAMINHO_ARQUIVO)
        else:
            print()
            print('TAREFAS:')
            print('Não a nada para desfazer!')
            print()

    elif comando == 'refazer':
        if refazer_tarefas:
            apagado = refazer_tarefas.pop()
            tarefas.append(apagado)
            print('TAREFAS:')
            for tarefa in tarefas:
                print(tarefa)
            salvar(tarefas, CAMINHO_ARQUIVO)
    elif comando == 'sair':
        break

    elif comando:
        tarefas.append(comando)
        salvar(tarefas, CAMINHO_ARQUIVO)
