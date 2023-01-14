class Pessoas:
    ANO_ATUAL = 2023

    def __init__(self, nome, idade, ano_nasc=2000):
        self.nome = nome 
        self.idade = idade 
        self.ano_nasc = ano_nasc

    def exibir_dados(self):
        print(f'nome: {self.nome}')
        print(f'idade: {self.idade}')
    
    @classmethod
    def criar_pessoa(cls, idade):
        nome = 'Alex'
        idade = idade
        ano_nasc = cls.ANO_ATUAL - idade

        return cls(nome, idade, ano_nasc)
    
    @staticmethod
    def mostrar():
        print('olá')


p1 = Pessoas.criar_pessoa(22)
p2 = Pessoas('anna', 18)

print(p1.__dict__)
print(vars(p2))

p1.mostrar()
