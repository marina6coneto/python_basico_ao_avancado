# Introdução à função lambda (função anônima de uma linha)
# A função lambda é uma função como qualquer
# outra em Python. Porém, são funções anônimas
# que contém apenas uma linha. Ou seja, tudo
# deve ser contido dentro de uma única
# expressão.
# lista = [
#     {'nome': 'Luiz', 'sobrenome': 'miranda'},
#     {'nome': 'Maria', 'sobrenome': 'Oliveira'},
#     {'nome': 'Daniel', 'sobrenome': 'Silva'},
#     {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
#     {'nome': 'Aline', 'sobrenome': 'Souza'},
# ]

# lista = [1, 7, 3, 8, 4, 0]
# lista.sort(reverse = True)
# print(lista)

lista = [
     {'nome': 'Luiz', 'sobrenome': 'Miranda'},
     {'nome': 'Maria', 'sobrenome': 'Oliveira'},
     {'nome': 'Daniel', 'sobrenome': 'Silva'},
     {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
     {'nome': 'Aline', 'sobrenome': 'Souza'},
]

# def ordena(item):
#     return item ['nome']


# lista.sort(key = ordena)

# for item in lista:
#     print(item)
# print()
# def ordena(item):
#     return item ['sobrenome']


# lista.sort(key = ordena)

# for item in lista:
#     print(item)

def exibir(lista):
    for item in lista:
        print(item)
    print()
l1 = sorted(lista, key = lambda item: item ['nome'])
l2 = sorted(lista, key = lambda item: item ['sobrenome'])


exibir(l1)
exibir(l2)