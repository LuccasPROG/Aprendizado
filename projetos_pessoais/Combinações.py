#essas função ela combinas coisas otimo
from itertools import combinations, permutations, product
    
def intrega(intertols):
    print(*list(intertols), sep='\n')
    print()

pessoas = [
    'jão', 'maria', 'vanessa', 'valentina'
]

camisetas = [
    ['preta', 'branca'],
    ['p', 'g'],
    ]

# print(intrega(intertols.p))
# intrega(combinations(pessoas, 2))
# intrega(permutations(pessoas, 2))
intrega(product(*camisetas))