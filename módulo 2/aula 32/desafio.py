 #Exercício - Lista de tarefas com desfazer e refazer

import os

lista_de_tarefas = []
lista_desfazer = []


def desfazer_tarefa():
    os.system('clear')

    if len(lista_de_tarefas) >= 1:
        ultima_tarefa = lista_de_tarefas.pop()
        lista_desfazer.append(ultima_tarefa)
        return lista_de_tarefas

    return 'NÃO HÁ O QUE DESFAZER!'


def refazer_tarefa():
    os.system('clear')

    if len(lista_desfazer) >= 1:
        ultima_tarefa_desfeita = lista_desfazer.pop()
        lista_de_tarefas.append(ultima_tarefa_desfeita)
        return lista_de_tarefas

    return 'NÃO HÁ O QUE REFAZER!'


def listar_tarefa():
    os.system('clear')

    if len(lista_de_tarefas) == 0:
        print('NÃO HÁ TAREFAS!')
    else:
        print(lista_de_tarefas)


def exibir():
    print('Comando: Listar - Desfazer - Refazer')
    opcao = input('Digite uma tarefa ou comando: ').title()
 
    if opcao != 'Listar' and opcao != 'Desfazer' and opcao != 'Refazer':
        lista_de_tarefas.append(opcao)
        os.system('clear')
    elif opcao == 'Listar':
        listar_tarefa()
        print()
    elif opcao == 'Desfazer':
        print(desfazer_tarefa())
        print()
    else:
        print(refazer_tarefa())
        print()
   
    return exibir()


exibir()
