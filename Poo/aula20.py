#Polimorfismo em Pythin orienbtado a Objetos
from abc import ABC, abstractmethod
class Notificacao(ABC): 
    def __init__(self, mensagem) -> None:
        self.mensagem = mensagem
    
    @abstractmethod
    def enviar(self) -> bool:
        ...

class NotificaçãoEmail(Notificacao): 
    def enviar(self) -> bool:
        print('e-emil: enviando - ', self.mensagem)
        return True


class NotificaçãoSMS(Notificacao): 
    def enviar(self) -> bool:
        print('SMS: enviando - ', self.mensagem)
        return True
    
def notificar(notificacao:Notificacao):
    notificacao_enviada = notificacao.enviar()

    if notificacao_enviada:
        print('notificaçao enviada')
    else:
        print('notificaçao NÂO enviada')

notificação_email = NotificaçãoEmail('Teste Enviando para pichl')
notificar(notificação_email)
notificação_sms = NotificaçãoSMS('Teste Enviando para pichl')
notificar(notificação_sms)
