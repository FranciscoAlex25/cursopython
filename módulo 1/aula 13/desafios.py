'''
Faça um programa que pessa um número inteiro e informe se este número é ímpar
ou par. Caso o usuário não digite um número inteiro informe ao usuário que ele
não digitou um número inteiro.
'''

numero = input('Informe um número inteiro: ')

if numero[0] == '-' or numero[0] == '+':
    if numero[1:].strip().isnumeric():
        num = int(numero)
        if num % 2 == 0:
            print(f'{num} é par')
        else:
            print(f'{num} é ímpar')
    else:
        print('O valor digitado não é um número inteiro.')
else:
    if numero[0:].strip().isnumeric():
        num = int(numero)
        if num % 2 == 0:
            print(f'{num} é par')
        else:
            print(f'{num} é ímpar')
    else:
        print('O valor digitado não é um número inteiro.')


'''
Faça um programa que pergunte ao usuário a hora e, baseado no que for digitado,
apresente uma saudação. Ex.: Bom dia: 0-11, boa tarde: 12-17 e boa noite: 18-23.
'''


print()

hora = input('Que horas são? (Digite com números (Ex.: 13:00, 9:00...)): ')

if hora[0:1].isnumeric():
    
    hora = hora[0:2]
    hora = int(hora)
    if hora <= 24:
        if hora == 24:
            hora = 0
            
        if hora >= 0 and hora <= 11:
            print('Bom dia!')
        elif hora >= 12 and hora <= 17:
            print('Boa tarde!')
        else:
            print('Boa noite')
    else:
        print('Informe uma hora válida de 1:00 às 24:00!')
else:
    print('Hora inválida!')


'''
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver quatro
letras ou menos mostre: seu nome é curso; Se tiver de 5 a 6 letras mostre: seu
nome é normal. Maior que 6 letras: seu nome é grande. 
'''

nome = input('Informe seu primeiro nome: ')

tamanho = len(nome.strip())

if tamanho <= 4:
    print('Seu nome é curto.')
elif tamanho > 5 and tamanho <= 6:
    print('Seu nome é normal')
else:
    print('Seu nome é grande.')
