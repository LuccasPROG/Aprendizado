# Mantendo estados dentro da classe

class Camera:
    def __init__(self, nome, filmando=False):
        self.nome = nome   
        self.filmando = filmando

    def filmar(self):
        if self.filmando:
            print(f'{self.nome} JÀ está filmando ...')
            return

        print(f'{self.nome} está filmando ...')
        self.filmando = True


    def fotografando(self):
        if self.filmando:
            print(f'{self.nome} Não pode fotografar filmando ...')
            return

        print(f'{self.nome} está fotografando agora ...')


    def parar_filmar(self):
        if not self.filmando:
            print(f'{self.nome} Não esta mais filmando ...')
            return

        print(f'{self.nome} está parando de filmando ...')
        self.filmando = False


camera_1 = Camera('Sony')
camera_2 = Camera('Cannon')

camera_1.filmar()
camera_1.filmar()
camera_1.fotografando()
camera_1.parar_filmar()
camera_1.parar_filmar()
camera_1.fotografando()

# camera_2.filmar()
# print(camera_2.filmando)