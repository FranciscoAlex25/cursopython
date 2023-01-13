class Carro:
    def __init__(self, nome):
        self.nome = nome

    def acelerar(self):    
        return f'{self.nome} está acelerando'


carro1 = Carro('fusca')
carro2 = Carro('gol')

print(f'carro: {carro1.nome} - aceleração: {carro1.acelerar()}')
print(f'carro: {carro2.nome} - aceleração: {carro2.acelerar()}')
