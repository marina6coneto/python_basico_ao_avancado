# json.dumps e json.loads com strings + typing.TypedDict
# Ao converter de Python para JSON:
# Python        JSON
# dict          object
# list, tuple   array
# str           string
# int, float    number
# True          true
# False         false
# None          null

import json
from pprint import pprint
from typing import TypedDict

class Movie(TypedDict):
    title: str
    original_title: str
    is_movie: bool
    imdb_rating: float
    year: int
    characters: list[str]
    budget: None | float


string_json = '''
{
    "title": "Harry Potter e as Relíquias da Morte - Parte 1",
    "original_title": "Harry Potter and the Deathly Hallows - Part 1",
    "is_movie": true,
    "imdb_rating": 7.7,
    "year": 2010,
    "characters": ["Harry", "Ron", "Hermione", "Voldemort", "Dumbledore"],
    "budget": null
  }
  
'''

filme: Movie = json.loads(string_json)

# pprint(filme, width=50)
# print(filme['title'])
# print(filme['characters'][2])
# print(filme['imdb_rating'])
# print(filme['year']+10)
json_string = json.dumps(filme, ensure_ascii=False, indent=2)
print(json_string)











