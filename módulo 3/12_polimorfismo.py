from abc import ABC, abstractmethod


class Notificacao(ABC):
    def __init__(self, mensagem) -> None:
        self.mensagem = mensagem
    
    @abstractmethod
    def enviar_mensagem(self): ...


class NotificacaoEmail(Notificacao):
    def enviar_mensagem(self):
        print('EMAIL:', self.mensagem)


notificacao = NotificacaoEmail('testando')
notificacao.enviar_mensagem()
