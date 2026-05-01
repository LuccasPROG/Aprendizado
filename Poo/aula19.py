from abc import ABC, abstractmethod


class AbstractFoo(ABC):
    def __init__(self, name):
        self._name = None
        self.name = name
    
    @property
    @abstractmethod
    def name(self):...

    @name.setter
    def name(self,name):
        self._name = name


class Foo(AbstractFoo):
    def __init__(self, name):
        super().__init__(name)
        # print('eu sou inutil')

foo = Foo('bar')
print(foo.name)