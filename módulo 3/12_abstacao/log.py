# Abstração 

class Log:
    def log(self, msg):
        raise NotImplementedError('Implemente o método log!')

    def error_message(self, msg):
        return self.log(f'ERROR: {msg}')

    def success_message(self, msg):
        return self.log(f'SUCCESS: {msg}')


class LogFileMixin(Log):
    def log(self, msg):
        print(f'{msg} {self.__class__.__name__}')


class LogPrintMixin(Log):
    def log(self, msg):
        print(msg)


if __name__ == '__main__':
    log1 = LogPrintMixin()
    log1.success_message('qualquer coisa')
