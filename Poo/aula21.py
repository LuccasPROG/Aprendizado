class MyError(Exception):
    ...



def levantar():
    raise MyError('A mensagem do meu erro')

levantar()


