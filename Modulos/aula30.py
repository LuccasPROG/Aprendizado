from threading import Thread
from time import sleep

def vai_demorar(texto, tempo):
    sleep(tempo)
    print(texto)

t = Thread(target=vai_demorar, args=('Ola, Mundo', 5))
t.start()


while t.is_alive():
    print('Esperando a thread.')
    sleep(2)

# for  i in range(20):
#     print(i)
#     sleep(.5)