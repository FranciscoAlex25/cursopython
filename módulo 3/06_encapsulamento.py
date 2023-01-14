class Fool:
    def __init__(self):
        self.public = 'publico'
        self._protect = 'protegido' # classe e subclasses
        self.__private = 'privado' # apenas na classe

    def _metodo_protegido(self):
        return '_metodo_protegido'
    
    def __metodo_privado(self):
        return '_metodo_privado'


fq = Fool()

print(fq._metodo_protegido())
print(fq._protect, fq.public)
