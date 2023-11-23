"""
Imprecisão de ponto flutuante
Double-precision floating-point format IEEE 754
https://en.wikipedia.org/wiki/Double-precision_floating-point_format
https://docs.python.org/pt-br/3/tutorial/floatingpoint.html
"""
import decimal

n1 = decimal.Decimal(0.1)
n2 = decimal.Decimal(0.7)
n3 = n1 + n2 
print(n3)
print(f'{n3:.2f}')
print(round(n3, 4))
n11 = decimal.Decimal('0.1')
n22 = decimal.Decimal('0.7')
n33 = n11 + n22 
print(n33)
print(f'{n33:.2f}')
print(round(n33, 4))