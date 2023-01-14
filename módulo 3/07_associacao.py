class Escritor:
    def __init__(self, nome):
        self._nome = nome
        self._maquina = None 

    @property
    def nome(self):
        return self._nome
    
    @property
    def maquina(self):
        return self._maquina

    @nome.setter
    def nome(self, nome):
        self._nome = nome
    
    @maquina.setter
    def maquina(self, maquina):
        self._maquina = maquina


class FerramentaDeEscrever:
    def __init__(self, nome):
        self.nome = nome

    def escrever(self):
        return f'{self.nome} está escrevendo'


escritor1 = Escritor('Pedro')
ferramenta1 = FerramentaDeEscrever('caneta')

escritor1.maquina = ferramenta1

print(escritor1.maquina.escrever())
print(ferramenta1.escrever())
