"""
Flag (Bandeira) - Marcar um local
None = Não valor
is e is not = é ou não é (tipo, valor, identidade)
id = Identidade
"""

condicao = True
passou_if = None
if condicao:
    passou_if = True
    print('Faça algo')
else:
    print('Não faça algo')
    
print(passou_if, passou_if is None)
print(passou_if, passou_if is not None)
