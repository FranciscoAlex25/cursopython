class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome 
        self.idade = idade 
    
    def falar(self):
        print(f'{__class__.__name__} está falando')


class Cliente(Pessoa): 

    def falar(self):
        print(f'{__class__.__name__} está falando')
        return ''


Cliente1 = Cliente('alex', 22)

print(Cliente1.falar())
print(Cliente1.nome, Cliente1.idade)

help(Cliente)
