from abc import ABC, abstractmethod


class Pessoa(ABC):
    def __init__(self):
        ...

    @abstractmethod
    def falar(self, nome):
        ...

    def obter_nome(self):
        frase = f'{self.__class__.__name__} está falando'

        return self.falar(frase)


class Cliente(Pessoa):
    def falar(self, nome):
        print(nome)


class Gerente(Pessoa):
    def falar(self, nome):
        print(nome)


Cliente().obter_nome()
Gerente().obter_nome()
