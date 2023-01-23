from log import LogFileMixin


class SmartPhone:
    def __init__(self, nome):
        self.nome = nome 
        self.ligado = False
        self.log = LogFileMixin()

    def ligar(self):
        if self.ligado == False:
            self.ligado = True
            self.log.success_message(f'{self.nome} está ligado')
        else:
            self.log.error_message(f'{self.nome} "está ligado já')


    def desligar(self):
        if self.ligado == True:
            self.ligado = False
            self.log.success_message(f'{self.nome} está desligado')
        else:
            self.log.error_message(f'{self.nome} está desligado já')
