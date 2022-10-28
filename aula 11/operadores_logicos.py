# operadores lógicos

'''
and, or, not, in, not in
'''

nome = 'André da Silva Oliveira'
idade = 22

print('Nome: ', nome)
print()

print(f'André está em nome: {"André" in nome}')
print(f'André não está em nome: {"André" not in nome}')
print(f'andré está em nome: {"andré" in nome}')

print()

if not idade < 18:
    print(f'{nome} é maior de idade')
