 #Exercício - Lista de tarefas com desfazer e refazer

import os, json 

lista_de_tarefas = []
lista_desfazer = []
caminho = os.path.dirname(__file__ + '/')


def desfazer_tarefa():
    os.system('clear')

    if len(lista_de_tarefas) >= 1:
        ultima_tarefa = lista_de_tarefas.pop()
        lista_desfazer.append(ultima_tarefa)
        print()
        return lista_de_tarefas
    print()
    return 'NÃO HÁ O QUE DESFAZER!'


def cadastrar_tarefa(opcao):
    lista_de_tarefas.append(opcao)
    os.system('clear')


def refazer_tarefa():
    os.system('clear')

    if len(lista_desfazer) >= 1:
        ultima_tarefa_desfeita = lista_desfazer.pop()
        lista_de_tarefas.append(ultima_tarefa_desfeita)
        print()
        return lista_de_tarefas
    print()
    return 'NÃO HÁ O QUE REFAZER!'


def listar_tarefa():
    os.system('clear')

    if len(lista_de_tarefas) == 0:
        print('NÃO HÁ TAREFAS!')
    else:
        print(lista_de_tarefas)


def conver_json():
    with open(caminho + 'arquivo.json', 'w') as arquivo:
        json.dump(lista_de_tarefas, arquivo)


def exibir():
    print('Comando: Listar - Desfazer - Refazer')
    opcao = input('Digite uma tarefa ou comando: ').title()
    
    try:
        comandos = {
            'Listar': lambda: listar_tarefa(),
            'Desfazer': lambda: print(desfazer_tarefa()),
            'Refazer': lambda: print(refazer_tarefa())
        }
        comando = comandos.get(opcao)()
    except:
        cadastrar_tarefa(opcao)

    conver_json()
    return exibir()


exibir()
