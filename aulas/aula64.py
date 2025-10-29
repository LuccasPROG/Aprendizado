#Exercicio - Salve sua classe em JSON
#Salve os dados da sua classe em JSON
#e depois crie novamente as instâncias da classe 
#com os dados salvos
#Faça em arquivos separados.
import json
CAMINHO_DO_ARQUIVO = 'aula64.json'


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

p1 = Pessoa('Carlos', 10)
p2 = Pessoa('Gabriele', 18)
dados = p1.__dict__, vars(p2)

def fazer_dump():
    with open(CAMINHO_DO_ARQUIVO, 'w', encoding='utf8') as arquivo:
        print('Fazendo Dump')   
        json.dump(dados, arquivo, indent=2)

if __name__ == '__MAIN__':
    print('Ele é o __MAIN__')
    fazer_dump()