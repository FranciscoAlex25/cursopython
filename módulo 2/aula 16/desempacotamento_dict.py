pessoa = {
    'nome': 'alex', 
    'sexo': 'masculino', 
    'idade': 22
}

locais = {
    'cidade': 'São Paulo', 
    'rua': 'São Marcos'
}

dados_gerais = {
    **pessoa, ** locais
}


# print(dados_gerais)

valores = lambda **kwargs: kwargs 

valor = valores(**dados_gerais)

for chave, valor in valor.items():
    print(chave, valor)

