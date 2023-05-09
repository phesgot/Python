# json.dump e json.load com arquivos
import json
import os
from pprint import pprint


NOME_ARQUIVO = '14 - json.dump e json.load com arquivos.json'
CAMINHO_ABSOLUTO_DO_ARQUIVO = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        NOME_ARQUIVO
    )
)

filme = {
    'title': 'O Senhor dos Anéis: A Sociedade do Anel',
    'original_title': 'The Lord of the Rings: The Fellowship of the Ring',

    'is_movie': True,
    'imdb_rating': 8.8,
    'year': 2001,
    'characters': ['Frodo', 'Sam', 'Gandalf', 'Legolas', 'Boromir'],
    'budget': None
}

with open(CAMINHO_ABSOLUTO_DO_ARQUIVO, 'w', encoding='utf8') as arquivo:
    json.dump(filme, arquivo, ensure_ascii=False, indent=2)

with open(CAMINHO_ABSOLUTO_DO_ARQUIVO, 'r', encoding='utf8') as arquivo:
    filme_do_json = json.load(arquivo)


pprint(filme_do_json)
