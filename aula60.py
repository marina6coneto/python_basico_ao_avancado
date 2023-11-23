"""
enumerate - enumera iteráveis (índices)
"""
lista = ['Marina', 'Felipe', 'Avaí']
lista.append('Ressacada')

# for indice, nome in enumerate(lista):
#     print(indice, nome)

for tupla_enumerada in enumerate(lista):
    print('FOR DA TUPLA: ')
    for valor in tupla_enumerada:
        print(f'\t{valor}')