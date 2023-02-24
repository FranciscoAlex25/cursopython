def repr_(self):
    return f'Classe {self.__class__.__name__}({vars(self)})'


class MetaClass(type):
    def __new__(mcs, name, base, dicts):
        print('CONSTRUTOR DA METACLASSE')
        instancia = super().__new__(mcs, name, base, dicts)
        instancia.__repr__ = repr_
        return instancia
    
    def __call__(cls, *args, **kwds):
        cls_ = super().__call__(*args, **kwds)
        print('CALL DA METACLASSE')
        print(cls_.__dict__)

        if 'nome' in cls_.__dict__:
            print('Tem o atributo Nome')
        else:
            print('Não tem o atributo nome')

        return cls_


class Pessoa(object, metaclass=MetaClass):
    def __new__(cls, *args, **kwargs):
        print('CONSTRUTOR DA INSTÂNCIA')
        return super().__new__(cls)
    
    def __init__(self):
        print('INIT DA INSTÂNCIA')
        self.nome = 'Alex'

    def falar(self):
        print('falando')


a = Pessoa()
