import json

# pessoa = {
#     'nome': 'Marina',
#     'sobrenome': 'Cesconeto dos Santos',
#     'enderecos': [
#         {'rua': 'Edeling Schutz', 'numero': '58'},
#         {'rua': 'Rua 2', 'numero': '00'}
#     ],
#     'altura': 1.66,
#     'numeros_preferidos': (5, 6, 10, 16),
#     'dev': True,
#     'nada': None,
    
# }

# with open('aula107.json', 'w', encoding='utf8') as arquivo:
#     json.dump(
#         pessoa,
#         arquivo,
#         ensure_ascii=False,
#         indent=2
#     )
    
with open('aula107.json', 'r', encoding='utf8') as arquivo:
    pessoa = json.load(arquivo)
    print(pessoa['nome'])