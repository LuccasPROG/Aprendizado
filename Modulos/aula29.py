from threading import Thread
from time import sleep

class MeuThred(Thread):
    def __init__(self, texto, tempo):
        self.texto = texto
        self.tempo = tempo

        super().__init__()
    
    def run(self):
        sleep(self.tempo)
        print(self.texto)
    
t1 = MeuThred('thread 1', 5)
t1.start()

for i in range(20):
    print(i)
    sleep(1)