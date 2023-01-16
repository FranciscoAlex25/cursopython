class carro:
    def __init__(self, nome):
        self.nome = nome
        self.motor = None 
        self.Fabricante = None

    def exibir_dados(self):
        print(f'Carro {self.nome} com motor {self.motor.nome} de fabricante {self.Fabricante.nome}')


class Motor:
    def __init__(self, nome):
        self.nome = nome 


class Fabricante:
    def __init__(self, nome):
        self.nome = nome 


motor1 = Motor('motor1')
fabricante1 = Fabricante('frab. 1')
carro = carro('fusca')

carro.motor = motor1 
carro.Fabricante = fabricante1

carro.exibir_dados()
