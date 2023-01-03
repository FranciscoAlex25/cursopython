import pprint

produto = {
    'nome': 'caneta', 
    'preco': 2.35, 
    'modelo': 'bic'
}

novo_dict = {
    chave: valor.upper() if isinstance(valor, str) else valor for chave, valor in produto.items() 
}

# print(novo_dict)

pprint.pprint(novo_dict, sort_dicts=True)
