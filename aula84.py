# Métodos úteis dos dicionários em Python

p1 = {
    'nome': 'Marina',
    'sobrenome': 'Cesconeto',
}

# get - obtém uma chave
print(p1.get('nome'))

# pop - Apaga um item com a chave especificada (del)
nome = p1.pop('nome')
print(nome)
print(p1)

# popitem - Apaga o último item adicionado
ultima_chave = p1.popitem()
print(ultima_chave)
print(p1)

# update - Atualiza um dicionário com outro
p1.update({
    'nome': 'novo valor',
    'idade': 20,
})
print(p1)

p1.update(nome='novo valor', idade=20)
print(p1)

tupla = ('nome', 'novo valor'), ('idade', 20)
p1.update(tupla)
print(p1)

lista = [['nome', 'novo valor'], ['idade', 20]]
p1.update(lista)
print(p1)