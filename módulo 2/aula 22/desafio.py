'''
# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)
'''

import copy, math

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90}
]

novos_produtos = [
    {**produto, 'preco': round(produto['preco'] * 1.01, 2)} for produto in produtos
]

ordenado_nome = sorted(novos_produtos, key=lambda item: item['nome'], reverse=True)
ordenado_preco = sorted(novos_produtos, key=lambda item: item['preco'])

produtos_ordenados_por_nome = copy.deepcopy(ordenado_nome)
produtos_ordenados_por_preco = copy.deepcopy(ordenado_preco)


def exibirDados(*lista):
    for i in lista:
        a, b = i.items()
        print(*a, *b)


exibirDados(*produtos_ordenados_por_nome)
print(50 * '-')
exibirDados(*produtos_ordenados_por_preco)
