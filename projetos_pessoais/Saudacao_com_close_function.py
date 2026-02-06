def criar_saudacao(saudacao):
    def saudar(nome):
        print(f'{saudacao}, {nome}')
    return saudar

falar_bom_dia = criar_saudacao('Bom Dia')
falar_boa_noite = criar_saudacao('Boa Noite')

falar_bom_dia('Lucas')
falar_boa_noite('Lucas')