"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""


def soma (x, y, z):
    # definição
    print(f'{x=} + y={y} + {z=} | x + y + z = ', x + y + z)
    
soma(4, 7, 6)
soma(y=2, x=5, z=6)

# se voce nomear um parametro na execução da função, 
# todos os outros parametros terão que ser nomeados também
# segue exemplo abaixo

soma(2, z=3, y=9)

# o z foi nomeado antes do y, entao o y tbm foi nomeado!

