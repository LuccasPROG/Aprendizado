# Implementando o protocolo do Iterator em Python
# Essa é apenas uma aula para introduzir os protocolos de collections.abc no
# Python. Qualquer outro protocolo poderá ser implementando seguindo a mesma
# estrutura usada nessa aula.
# https://docs.python.org/3/library/collections.abc.html

from collections.abc import Sequence
from typing import Iterator

class Mylist(Sequence):
    def __init__(self) -> None:
        self._data = {}
        self._index = 0

    def append(self, *value):
        for item in value:
            self._data[self._index] = value
            self._index += 1
    
    def __len__(self) -> int:
        return self._index

    def __getitem__(self, index) -> Sequence:

        return self._data[index]
    
    def __setitem__(self, index, value):
        self._data[index] = value

    def __iter__(self) -> Iterator:
        self._next_index = 0
        return self
    
    def __next__(self):
        if self._next_index >= self._index:
            self._next_index = 0
            raise StopIteration

        value =  self._data[self._next_index]
        self._next_index += 1
        return value

if __name__ == '__main__':
    lista = Mylist()
    lista.append('MARIA', 'carlos')
    lista[0]= 'João'
    # print(lista[0])
    # print(len(lista))
    for item in lista:
        print(item)