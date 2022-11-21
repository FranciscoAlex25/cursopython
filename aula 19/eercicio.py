nome = input('Informe um nome próprio: ')

novo_nome = ''
cont = 0

while cont < len(nome):
    if cont == 0:
        novo_nome += f'*{nome[cont]}*'
    else:
        novo_nome += f'{nome[cont]}*'
    cont += 1

novo = novo_nome[0:-1]

print(novo)
