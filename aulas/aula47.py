# Combinations, Permutations e Product - Itertools

# Combinação - Ordem não importa - iterável + tamanho do grupo - não repetira palavras
# Permutação - Ordem importa # ent repetira as palavras ex joao e joana e joana e joao
# Produto - Ordem importa e repete valores únicos pode fazer combinações de coisas

from itertools import combinations, permutations, product

def print_iter(iteretor):
    print(*list(iteretor),sep='\n')

#INICIO:

pessoa = [
    'Suelen', 'Edson', 'Edna', 'Lucas', 'Valentina'
]
camisetas = [
    ['Preta', 'Branca'],
    ['P', 'M', 'G'],
    ['Masculino', 'Feminino', 'Unisex'],
    ['Algodão', 'Poliester'],
]

print_iter(combinations(pessoa, 2))
print()
print_iter(permutations(pessoa, 2))

print_iter(product(*camisetas))