# json.dump e json.load com arquivos
import json
import os

NOME_ARQUIVO = 'aula176.json'
CAMINHO_ABSOLUTO_ARQUIVO = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        NOME_ARQUIVO
    )
)

filme = {
    "title": "Harry Potter e as Relíquias da Morte - Parte 1",
    "original_title": "Harry Potter and the Deathly Hallows - Part 1",
    "is_movie": True,
    "imdb_rating": 7.7,
    "year": 2010,
    "characters": ["Harry", "Ron", "Hermione", "Voldemort", "Dumbledore"],
    "budget": None
}
  
with open(CAMINHO_ABSOLUTO_ARQUIVO, 'w') as arquivo:
    json.dump(filme, arquivo, ensure_ascii=False, indent=2)

with open(CAMINHO_ABSOLUTO_ARQUIVO, 'r') as arquivo:
    filme_do_json = json.load(arquivo)
    print(filme_do_json)