# Manipulando chaves e valores em dicionários

pessoa = {
    
}

chave = 'nome'
pessoa[chave] = 'Marina'
pessoa['sobrenome'] = 'Cesconeto'
lista = []

print(pessoa[chave])

pessoa[chave] = 'Felipe'

del pessoa['sobrenome']
print(pessoa)


#print(pessoa.get('sobrenome')) 
if pessoa.get('sobrenome') is None:
    print('NÃO EXISTE')
else:
    print(pessoa['sobrenome'])


