from threading import Thread
from time import sleep
from threading import Lock

class Ingresso:
    def __init__(self, estoque):
        self.estoque = estoque
        self.lock = Lock()
    
    def comprar(self, quantidade):
        self.lock.acquire()
        if self.estoque < quantidade:
            print('Não temos ingressos Suficiente!')
            self.lock.release()
            return
        
        self.estoque -= quantidade
        print(f'Você Comprou {quantidade} ingresso(s)'
              f'Ainda Temos {self.estoque} em estoque')
        
        self.lock.release()
        

if __name__ == '__main__':
    ingresso = Ingresso(10)

    for i in range(1, 20):
        t = Thread(target=ingresso.comprar, args=(i,))
        t.start()
        ingresso.comprar(i)
              