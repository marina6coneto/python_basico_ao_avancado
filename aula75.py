"""
args - Argumentos não nomeados
* - *args (empacotamento e desempacotamento)
"""
# lembre-te de desempacotamento

# x, y, *resto = 1, 2, 3, 4
# print(x, y, resto)

# def soma(x,y):
#     return x + y

def soma(*args):
    total = 0
    for numero in args:
        total += numero
    return total

soma_1_2_3 = soma(1,2,3)
print(soma_1_2_3)

soma_4_5_6_7 = soma(4,5,6,7)
print(soma_4_5_6_7)

numeros = 3,5,6,12,89
# outra_soma = soma(*numeros)
# print(outra_soma)
print(sum(numeros))