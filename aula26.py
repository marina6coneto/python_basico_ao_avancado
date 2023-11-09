"""
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o número a aparecer antes dos zeros
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a 
"""
variavel = 'abc'
print(f'{variavel:->10}')
print(f'{variavel:-<10}')
print(f'{variavel:-^10}')

print(f'{1000.783757453578:.1f}')
print(f'O hexadecimal de 1500 é {1500:08x}')
print(f'{variavel!r}')