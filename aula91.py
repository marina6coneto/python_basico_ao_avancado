# Empacotamento e desempacotamento de dicionários

# a, b = 1, 2
# a, b = b, a
# print(a, b)  empacotamento simples


# pessoa = {
#     'nome': 'Marina',
#     'sobrenome': 'Cesconeto',
# }

# a, b = pessoa
# print(a, b)

# a, b = pessoa.values()
# print(a, b)

# a, b = pessoa.items()
# print(a, b)


# (a1, a2), b = pessoa.items()
# print(a1, a2)

# (a1, a2), (b1, b2) = pessoa.items()
# print(a1, a2, b1, b2)


# for valor in pessoa.items():
#     print(valor)
    
# for chave, valor in pessoa.items():
#     print(chave, valor)
    
    
pessoa = {
    'nome': 'Marina',
    'sobrenome': 'Cesconeto',
} 

dados_pessoa = {
    'idade': 25,
    'altura': 1.66,
}

pessoa_completa = {**pessoa, **dados_pessoa}

#print(pessoa_completa)


# args e kwargs
# args (já vimos)
# kwargs - keyword arguments (argumentos nomeados)


def mostro_argumentos_nomeados(*args, **kwargs):
    #print('NÃO NOMEADOS: ', args)
    for chave, valor in kwargs.items():
        print(chave, valor)
    
    
#mostro_argumentos_nomeados(45, 74, nome = 'Felipe', idade = 23)
#mostro_argumentos_nomeados(**pessoa_completa)


configuracoes = {
    'arg1': 1,
    'arg2': 2,
    'arg3': 3,
    'arg4': 4,
}

mostro_argumentos_nomeados(**configuracoes)