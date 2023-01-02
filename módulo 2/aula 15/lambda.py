usuarios = [
    {'nome': 'alex', 'sobrenome': 'lima'}, 
    {'nome': 'ana', 'sobrenome': 'alves'},
    {'nome': 'pedro', 'sobrenome': 'aquino'}
]

# def ordenarUsuarios(items):
#     return items['sobrenome']

# usuarios.sort(key=ordenarUsuarios)

# for i in usuarios:
#     print(i)

ordenaNome = sorted(usuarios, key=lambda item: item['nome'])
ordenaSobrenome = sorted(usuarios, key=lambda item: item['sobrenome'])

def exibirLIsta(*lista):
    for i in lista:
        print(i)
    

print(ordenaNome)

exibirLIsta(*ordenaNome)
