import os

def listar_tarefa(args):
    if not args:
        print('Nada para listar')
    print(*args, sep='\n')


def desfazer_tarefa(tarefas, hist_tarefas):
    if not tarefas:
        print('Nada para defazer')
        return
    
    hist_tarefas.append(tarefas[-1])
    del tarefas[-1]
    listar_tarefa(tarefas)


def refazer_tarefa(tarefas, hist_tarefas):
    if not hist_tarefas:
        print('Nada para refazer')

    tarefas.append(hist_tarefas[-1])
    del hist_tarefas[-1]
    listar_tarefa(tarefas)


def adicionar_tarefa(tarefa, tarefas):
    if tarefa is not None:
        tarefas.append(tarefa)

    listar_tarefa(tarefas)


def controle_tarefas():
    tarefas = []
    hist_tarefas = [] 

    while True:
        comando = input(str('Comandos:  listar, desfazer, refazer, sair: ')).strip().lower()
        if comando == 'listar':
            listar_tarefa(tarefas)
        elif comando == 'desfazer':
            desfazer_tarefa(tarefas, hist_tarefas)
        elif comando == 'refazer':
            refazer_tarefa(tarefas, hist_tarefas)
        elif comando == 'sair':
            break
        elif comando == 'clear':
            os.system('clear')
        else:
            adicionar_tarefa(comando, tarefas)

        print()


controle_tarefas()