from datetime import datetime

nome = str(input(f'Nome:'))
sobrenome= str(input(f'Sobrenome:'))
ano_nasc = int(input(f'Ano de nascimento:'))
idade = datetime.now().year - ano_nasc 
altura = float(input(f'Altura em metros:'))

print('-='*10)
print('  Analize de Dados')
print('-='*10)
print(f'O nome é {nome}')
print(f'O sobrenome é {sobrenome}')
print(f'O ano de nascimento é {ano_nasc}')
print(f'Idade é {idade}')
if idade >= 18:
    print('Você é maior de idade!')
else:
    print('Você não é maior de idade!')
print(F'A Altura é {altura}')
print('-='*10)