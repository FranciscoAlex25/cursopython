# ---------------------------------INTRODUZINDO-------------------------
# lista1 = [i * 2 for i in range(5)]
# lista2 = []

# for i in range(5):
#     lista2.append(i)

# print(lista1)
# print(lista2)

# ----------------------------MAPEAMENTO--------------------------------
# produtos = [
#     {'nome': 'arroz', 'preco': 10}, 
#     {'nome': 'crne', 'preco': 30}, 
#     {'nome': 'feijão', 'preco': 18}
# ]

# for i in produtos:
#     i['preco'] = i['preco'] - (5 * i['preco']  / 100)
#     produtos_com_descontos.append({**i})

# produtos_com_descontos = [
#     {**i, 'preco': i['preco'] * 0.95} for i in produtos
# ]

# print(produtos_com_descontos)

# -------------------------------------------------------------

# nome = 'Francisco Alex'

# novo_nome = [letra.lower() if 'o' not in nome else letra.upper() for letra in nome]
# novo_nome = ''.join(novo_nome)

# print(novo_nome)

# -------------------------------------------------------------
