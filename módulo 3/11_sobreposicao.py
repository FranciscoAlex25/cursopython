class Pessoa:
    def __init__(self):
        ...
    
    def exibirAlgo(self):
        print('Olá, estou no método de Pessoa')


class Sub(Pessoa):
    def exibirAlgo(self):
        print('Estou no método de Sub')
        var = super().exibirAlgo()
        return var 


sub1 = Sub() 
sub1.exibirAlgo()
