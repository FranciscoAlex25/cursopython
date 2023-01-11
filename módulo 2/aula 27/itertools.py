from itertools import groupby
# from itertools import combinations, permutations, product

# ------------- Combinations, Permutations, Products ----------------------
# pessoas = [
#     'ana', 'alex', 'miguel', 'pedro'
# ]

# roupas = [
#     ['branca', 'preta'], 
#     ['M', 'G']
# ]

# def exibirDados(valores):
#     for i in valores:
#         print(i)


# # exibirDados(combinations(pessoas, 2))
# # exibirDados(permutations(pessoas, 2))
# exibirDados(product(*roupas))
# --------------------------------------------------------------------------

alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'André', 'nota': 'A'},
    {'nome': 'Anderson', 'nota': 'C'},
]

aluos_ordenados = sorted(alunos, key=lambda a: a['nota'])

ordenados = groupby(aluos_ordenados, key=lambda a: a['nota'])

for chave, valor in ordenados:
    print(chave)
    for i in valor:
        print(i['nome'], end=' ')
    print()
