def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}!'
    
    return saudar
    
#INICIO:
falar_bom_dia = criar_saudacao('Bom dia')
falar_boa_tarde = criar_saudacao('Boa tarde')
falar_boa_noite=  criar_saudacao('Boa noite')

for nome in ['Carlos', 'Lucas','suelen']:   
    print(falar_bom_dia(nome))
    print(falar_boa_tarde(nome))
    print(falar_boa_noite(nome))