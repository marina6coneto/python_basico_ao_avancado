"""
https://docs.python.org/pt-br/3/library/stdtypes.html
Imutáveis que vimos: str, int, float, bool
"""

string = 'Marina'
outra_variavel = f'{string[:3]}ABC{string[4:]}'


print(string)
print(outra_variavel)
#capitalize vem com a primeira letra maiúscula (ex: marina retorna Marina)

print(string.zfill(10)) #preenche com 'zeros' a esquerda.