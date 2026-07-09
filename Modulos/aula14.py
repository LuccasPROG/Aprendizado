# O que é JSON - JavaScript Object Notation
# JSON - JavaScript Object Notation (extensão .json)
# É uma estrutura de dados que permite a serialização
# de objetos em texto simples para facilitar a transmissão de
# dados através da rede, APIs web ou outros meios de comunicação.
# O JSON suporta os seguintes tipos de dados:
# Números: podem ser inteiros ou com ponto flutuante, como 42 ou 3.14
# Strings: são cadeias de caracteres, como "Olá, mundo!" ou "12345"
#   As strings devem ser envolvidas por aspas duplas
# Booleanos: são os valores verdadeiro (true) ou falso (false)
# Arrays: são listas ordenadas de valores, como [1, 2, 3] ou
#   ["Oi", "Olá", "Bom dia"]
# Objetos: são conjuntos de pares chave/valor -> {"nome": "João", "idade": 30}
# null: é um valor especial que representa ausência de valor
import json
import os
import pprint

NOME_ARQUIVO = 'aula14.json'
CAMINHO_ABSOLUTO_ARQUIVO = os.path.join(os.path.dirname(__file__), NOME_ARQUIVO)
filme = { 
    'title': 'O Senhor dos Anéis: A Sociedade do Anel',
    'original_title': 'The Lord of the Rings: The Fellowship of the Ring',

    'is_movie': True,
    'imdb_rating': 8.8,
    'year': 2001,
    'characters': ['Frodo', 'Sam', 'Gandalf', 'Legolas', 'Boromir'],
    'budget': None
}
print(CAMINHO_ABSOLUTO_ARQUIVO)

with open(CAMINHO_ABSOLUTO_ARQUIVO, 'w', encoding='utf8') as arquivo:
    json.dump(filme, arquivo, ensure_ascii=False, indent=2)

with open(CAMINHO_ABSOLUTO_ARQUIVO, 'r', encoding='utf8') as arquivo:
    filme_json = json.load(arquivo)
    pprint.pprint(filme_json)