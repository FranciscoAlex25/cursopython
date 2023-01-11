produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

def alterar(*valores):
    """ Esta função modifica o preço dos produtos em 10% """

    novos_produtos = [
        {**c, 'preco': c['preco'] * 1.1} for c in valores
    ]

    return novos_produtos


print(*list(map(
    alterar, produtos
)))

print(30 * '-')

print(
    list(filter(
        lambda x: x['preco'] > 20, 
        produtos
    ))
)

print(30 * '-')

