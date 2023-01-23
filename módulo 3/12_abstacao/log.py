# Abstração 
import os 

CAMINHO = os.path.dirname(__file__)


class Log:
    def log(self, msg):
        raise NotImplementedError('Implemente o método log!')

    def error_message(self, msg):
        return self.log(f'ERROR: {msg}')

    def success_message(self, msg):
        return self.log(f'SUCCESS: {msg}')


class LogFileMixin(Log):
    def log(self, msg):
        print(msg)

        retorno = f'{msg}'
        
        with open(CAMINHO + '/arquivo.txt', 'a+') as arquivo:
            arquivo.write(retorno)
            arquivo.write('\n')


class LogPrintMixin(Log):
    def log(self, msg):
        print(msg)

        retorno = f'{msg} {self.__class__.__name__}'
        
        with open(CAMINHO + '/arquivo.txt', 'a+') as arquivo:
            arquivo.write(retorno)
            arquivo.write('\n')



if __name__ == '__main__':
    log1 = LogFileMixin()
    log1.success_message('qualquer coisa')
