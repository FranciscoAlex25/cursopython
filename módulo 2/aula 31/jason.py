import json, os 

caminho = os.path.dirname(__file__ + '/')

pessoa = {
    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda',
    'enderecos': [
        {'rua': 'R1', 'numero': 32},
        {'rua': 'R2', 'numero': 55},
    ],
    'altura': 1.8,
    'numeros_preferidos': (2, 4, 6, 8, 10),
    'dev': True,
    'nada': None,
}


# with open(caminho + 'arquivo.json', 'w+', encoding='utf8') as arquivo:
#     json.dump(pessoa, arquivo, indent=2)

with open(caminho + 'arquivo.json', 'r', encoding='utf-8') as arquivo:
    var = json.load(arquivo)

    print(var)
