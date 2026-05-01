class Animal:
    def __init__(self, nome):
        self.nome = nome

        variavel = 'variavel'
        print(variavel)


    def comendo(self, alimento):
        return f'{self.nome} esta Comendo {alimento}'
    
    def executar(self, *args, **kwargs):
        return self.comendo(*args, **kwargs)
    
leao = Animal('leao')
print(leao.nome)  
print(leao.executar('carne'))