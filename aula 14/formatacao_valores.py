# Formatação de valores

'''
:s
:d
:f
:.(NÚMERO) - Quantidade de casas decimais (float)
:(CARACTERE) (> ou < ou ^) (QUANTIDADE)(TIPO -s, d ou f)

> - esquerda
< - direita
^ - centro
'''

num = 1
nome = 'Alex'
peso = 50

print(f'{num:-^10}')
print(f'{nome:-^10}')
print(f'{nome:*<10}')

print()

print(f'{peso:0>7.2f}')
