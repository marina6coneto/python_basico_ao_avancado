"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""

# print(123)
# print(456)
# int('a')

# num = float(input('Vou dobrar o número que você digitar: '))
# print(f'O dobro de {num} é {num*2:.2f}')

num_str = input(
    'Vou dobrar o número que você digitar: '
)

# if num_str.isdigit():
#     num_float = float(num_str)
#     print(f'O dobro de {num_str} é {num_float*2:.2f}')
# else:
#     print('Isso não é um número.')

try:
    print(f'String: {num_str}')
    num_float = float(num_str)
    print(f'O dobro de {num_str} é {num_float*2:.2f}')

except:
    print('Isso não é um número.')
    