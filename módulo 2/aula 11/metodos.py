pessoas = {
    'nome': 'alex', 
    'idade': 22, 
    'sexo': 'masculino', 
    'endereço': [
        {
            'rua': 'rua zero',
            'bairro': 'do nada'
        }
    ]
}

# print(pessoas.keys())
# print(pessoas.values())
# print(pessoas.items())

for chave, valor in pessoas.items(): 
    if chave == 'endereço':
        for i in pessoas['endereço']:
            for c, v in i.items():
                print(f'{c}: {v}')
    else:
        print(f'{chave}: {valor}')
