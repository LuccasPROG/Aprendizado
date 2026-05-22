class CallMe:
    def __init__(self, phone):
        self.phone = phone

    def __call__(self, *args, **kwds):
        print('Chamando', self.phone)
call1 = CallMe('252164584694')
call1()