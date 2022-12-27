# Quantificar caracteres

nome = input('Informe uma frase com até 8 caracteres: ')

if len(nome) <= 8:
    print(f'{nome}. tamanaho: {len(nome)}')
else:
    print(f'Ultrapassou 8 caracteres. tamanaho: {len(nome)}')
