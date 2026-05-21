class MyError(Exception):
    ...
class Outroerror(Exception):
    ...



def levantar():
    exception_ = MyError('A mensagem do meu erro')
    exception_.add_note('VOcê errou isso !!')
    raise exception_

try:
    levantar()
except (MyError, ZeroDivisionError) as error:
    print(error.__class__.__name__)
    print(error.args)
    print()
    exception_ = Outroerror('vou lançar de novo')
    exception_.__notes__ = error.__notes__.copy()
    exception_.add_note('mais um error!')
    raise exception_ from error


