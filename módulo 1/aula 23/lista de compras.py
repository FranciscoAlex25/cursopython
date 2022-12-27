lista = []
import os 

while True:
    print('[1]Inserir - [2]Apagar - [3]Listar')
    valor = input('Digite a opção desejada: ')

    if valor == '1' or valor == '2' or valor == '3':
        if valor == '1':
            produto = input('Informe um produto: ')
            lista.append(produto)
            os.system('clear')
        elif valor == '2':
            prodApagar = input('Qual o índice que deseja apagar: ')
            if prodApagar.isnumeric() and int(prodApagar) < len(lista):
                for i in enumerate(lista):
                    if prodApagar in i:
                        lista.pop(prodApagar)
                        os.system('clear')
            else:
                print('Valor de índice inválido!')
        else:
            for i, p in enumerate(lista):
                print(i, p)
    else:
        print('Opção inválida!')
