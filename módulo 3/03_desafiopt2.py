import json, os 

caminho = os.path.dirname(__file__)

with open(caminho + '/03_desafiopt1.pyclasse.json', 'r', encoding='utf8') as arquivo:
    dados = json.load(arquivo)


class Animal:
    def __init__(self, nome, idade):
        self.nome = nome 
        self.idade = idade 


animal1 = Animal(dados['nome'], dados['idade'])

print(animal1.nome, animal1.idade)
