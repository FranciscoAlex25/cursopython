# Operadores relacionais

'''
<, >, <=, >=, ==, != 
'''

idade = input('Informe sua idade: ')

if idade.isnumeric():
    idade = int(idade)
    if idade < 0:
        print('Idade inválida.')
    elif idade < 18:
        print('Vocẽ é menor de idade.')
    else:
        print('Você é maior de idade.')
else:
    print('Idade inválida!')
