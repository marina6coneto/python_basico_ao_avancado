"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::] i = inicio f = fim p =passo
Obs.: a função len retorna a qtd 
de caracteres da str
"""

variavel = 'Olá mundo'
print(variavel[5])
print(variavel[2])

print(variavel[4:])
print(variavel[:5])
print(len(variavel))
print(len(variavel[4:]))
print(variavel[0:9:3])
print(variavel[-1:-10:-1])