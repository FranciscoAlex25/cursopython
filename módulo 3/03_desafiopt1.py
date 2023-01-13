import json, os 

caminho = os.path.dirname(__file__ + '/')


class Animal:
    def __init__(self, nome, idade):
        self.nome = nome 
        self.idade = idade


animal1 = Animal('leão', 8)
dados = vars(animal1)

with open(caminho + 'classe.json', 'w+', encoding='utf8') as arquivo:
    json.dump(dados, arquivo)
