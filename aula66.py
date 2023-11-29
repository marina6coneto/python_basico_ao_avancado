# Desempacotamento em chamadas
# de métodos e funções

# string = 'ABCD'
# lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
# tupla = 'Python', 'é', 'legal'

# # a, b, c = lista
# # print(a, c)

# for nome in lista:
#     print(nome)
    
    
# print(*lista)

salas = [
    #  0           1
    ['Maria', 'Helena'], #0
    #0
    ['Elaine',],#1
    #0          1       2
    ['Luiz', 'João', 'Eduarda', (0, 10, 20, 30, 40)],#2
]


print(*salas, sep='\n')