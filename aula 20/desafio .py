# Exercício de tabuada

valor = int(input('Qual tabuada deja calcular? '))
opr = input('Qual operação deseja? (+, -, /, x)')
cont= 1

if opr == '+':
    while cont <= 10:
        print(f'{valor} + {cont} = {valor + cont}')
        cont += 1

if opr == '-':
    while cont <= 10:
        print(f'{valor} - {cont} = {valor - cont}')
        cont += 1

if opr == '/':
    while cont <= 10:
        print(f'{valor} / {cont} = {valor / cont}')
        cont += 1

if opr == 'x':
    while cont <= 10:
        print(f'{valor} * {cont} = {valor * cont}')
        cont += 1

