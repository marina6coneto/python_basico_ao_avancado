"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

num_str  = input('Digite um número inteiro: ')

if num_str.isdigit():
    num_int = int(num_str)
    if num_int % 2 == 0:
        print('O número digitado é par.')
    else:
        print('O número digitado é impar.')
else: 
    print(f'{num_str} não é um número inteiro.')


