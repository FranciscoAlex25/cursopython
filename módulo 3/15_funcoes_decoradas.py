def repre(class_):
    def aux(*args, **kwargs):
        return f'{class_.__name__}{vars(class_(*args, **kwargs))}'
    return aux


@repre
class Pais(object):
    def __init__(self, nome) -> None:
        self.nome = nome 
    
    # def __repr__(self) -> str:
    #     self.retorno = f'{self.__class__.__name__}({vars(self)})'
    #     return self.retorno


@repre
class Planeta(object):
    def __init__(self, nome) -> None:
        self.nome = nome 
    
    # def __repr__(self) -> str:
    #     return f'{self.__class__.__name__}({vars(self)})'


Brasil = Pais('Brasil')
Franca = Pais('França')

Terra = Planeta('Terra')
Jupter = Planeta('Jupter')

print(Terra)
print(Jupter)

print(Brasil)
print(Franca)
