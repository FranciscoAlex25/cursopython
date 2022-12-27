# Trabalhando com condicionais

valor = input('Informe um número inteiro: ')

'''
string.isalpha()
string.isdecimal()
string.isdigit()
string.isnumeric()
string.isalnum()
string.isspace()
string.isprintable()
Bonus: string.isidentifier()
'''

'''
try:
    if int(valor):
        valor = float(valor)
        if valor % 2 == 0:
            print(f'{valor} é par')
        else:
            print(f'{valor} é ímpar')
except:
    print('Valor inválido!')
'''

if valor.isnumeric():
    valor = float(valor)
    if valor % 2 == 0:
        print(f'{valor} é par')
    else:
        print(f'{valor} é ímpar')
elif str(valor):
    print('Valor inválido')
