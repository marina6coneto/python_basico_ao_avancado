"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""

lista_a = ['Felipe', 'Marina', 1, True, 1.2]
lista_b = lista_a.copy()

lista_a[0] = 'Leite'
print(lista_b)
print(lista_a)