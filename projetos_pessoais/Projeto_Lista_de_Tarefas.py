import time
lista = []
def linha():
    print('-='*10)


def criar_lista(lista, nome):
    lista.append({
        'nome': nome,
        'concluida': False
    })
    print(f'\033[32mLista {nome} Criado com sucesso!\033[m')
    time.sleep(1)


def mostrar_lista(lista):
    linha()
    print('       LISTA')
    linha()

    if not lista:
        print('\033[33mNenhuma tarefa cadastrada!\033[m')
        return
    
    for i, tarefa in enumerate(lista):

        if tarefa['concluida']:
            stats = '\033[1;32mConcluida\033[m'
        else:
            stats = '\033[1;31mPendente\033[m' 
            
        print(f"{i + 1}. {tarefa['nome']} - {stats}")
        time.sleep(0.5)


def concluir_tarefas(indice, lista):
    if 0 <= indice < len(lista):
        lista[indice]['concluida'] = True
        print(f'\033[32m o numero {indice + 1} concluido com sucesso!\033[m')
        time.sleep(1)
    else:
        print('\033[1;31mERROR: Numero Invalido\033[m')


def remover_tarefa(indice, lista):
    if 0 <= indice < len(lista):
        lista.pop(indice)
        print(f'\033[32m o numero {indice + 1} removido com sucesso!\033[m')
        time.sleep(1)
    else:
        print('\033[1;31mERROR: Numero Invalido\033[m')


while True:
    print('-='*10)
    print('   MENU DE TAREFAS')
    print('-='*10)
    print('''
    1 - adicionar tarefa
    2 - listar tarefas
    3 - concluir tarefas
    4 - remover tarefas
    5 - sair
    ''')
    try:
        opcao = int(input('Opção:'))
    except ValueError:
        print('\033[31mERROR: Digite um Número inteiro!\033[m')
        time.sleep(1)
        continue
    if opcao == 1:
        try:
            nome = str(input('Digite o nome da tarefa que deseja iniciar:'))
            criar_lista(lista, nome)
        except ValueError:
            print('\033[31mERROR: Digite um Número inteiro!\033[m')
            time.sleep(1)
            continue
    elif opcao == 2:
        mostrar_lista(lista)
    elif opcao == 3:
        try:
            indice = int(input('Digite o numero da tarefa que deseja concluir:'))
            indice -= 1
            concluir_tarefas(indice, lista)
        except ValueError:
            print('\033[31mERROR: Digite um Número inteiro!\033[m')
            time.sleep(1)
            continue
    elif opcao == 4:
        try:
            remove = int(input('Digite o numero da tarefa que deseja remover:'))
            remove -= 1
            remover_tarefa(remove, lista)
        except ValueError:
            print('\033[31mERROR: Digite um Número inteiro!\033[m')
            time.sleep(1)
            continue
    elif opcao == 5:
        break



time.sleep(2)
print('-='*10)
print('Volte Sempre')
print('-='*10)