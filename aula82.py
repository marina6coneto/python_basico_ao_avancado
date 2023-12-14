# Métodos úteis dos dicionários em Python

pessoa = {
    'nome': 'Marina',
    'sobrenome': 'Cesconeto',
}

# len - quantas chaves
print(pessoa.__len__())
print(len(pessoa))

# keys - iterável com as chaves
print(pessoa.keys())

# values - iterável com os valores
print(pessoa.values())
for valor in pessoa.values():
    print(valor)

# items - iterável com chaves e valores    
print(pessoa.items())
for chave, valor in pessoa.items():
    print(chave, valor)

# setdefault - adiciona valor se a chave não existe    
pessoa.setdefault('idade', 25)    
print(pessoa['idade'])

