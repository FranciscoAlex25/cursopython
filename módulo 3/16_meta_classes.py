def repr_(self):
    return f'Classe {self.__class__.__name__}({vars(self)})'


class MetaClass(type):
    def __new__(mcs, name, base, dicts):
        print('CONSTRUTOR DA METACLASSE')
        instancia = super().__new__(mcs, name, base, dicts)
        instancia.__repr__ = repr_
        return instancia
    

class Pessoa(object, metaclass=MetaClass):
    def __new__(cls, *args, **kwargs):
        print('CONSTRUTOR DA INSTÂNCIA')
        return super().__new__(cls)
    
    def __init__(self):
        print('INIT DA INSTÂNCIA')



a = Pessoa()
print(a)
