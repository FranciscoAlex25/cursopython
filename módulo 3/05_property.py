class Caneta:
    def __init__(self, cor, marca):
        self._cor = cor 
        self._marca = marca
    
    @property
    def cor(self):
        self._cor = self._cor.upper()
        return self._cor
    
    @property
    def marca(self):
        self._marca = self._marca.upper()
        return self._marca

    @cor.setter
    def cor(self, valor):
        self._cor = valor

    @marca.setter
    def marca(self, valor):
        self._marca = valor


caneta1 = Caneta('azul', 'bic')

caneta1.cor = 'preta'
caneta1.marca = 'castle'

print(caneta1.cor)
print(caneta1.marca)
