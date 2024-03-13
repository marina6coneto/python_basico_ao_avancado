# Problema dos parâmetros mutáveis em funções Python
def adiciona_cliente(nome, lista=None):
    if lista is None:
        lista = []
    lista.append(nome)
    return lista

cliente_1 = adiciona_cliente('Marina')
adiciona_cliente('Felipe', cliente_1)
adiciona_cliente('Liliam', cliente_1)
cliente_1.append('Harry Potter')
print(cliente_1)

cliente_2 = adiciona_cliente('Valéria')
adiciona_cliente('Nazareno', cliente_2)
print(cliente_2)