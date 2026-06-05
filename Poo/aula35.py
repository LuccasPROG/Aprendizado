from dataclasses import dataclass, asdict, astuple


@dataclass()
class Pessoa:
    nome: str
    sobrenome: str


if __name__ == "__main__":
    p1 = Pessoa('Lucas', 'ovo')
    print(asdict(p1).keys())
    print(astuple(p1)[1])
    print(p1)