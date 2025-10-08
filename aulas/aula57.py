# Exercício - Lista de tarefas com desfazer e refazer
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']
import os
tarefas = []
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

    elif comando == 'sair':
        break

    elif comando:
        tarefas.append(comando)
