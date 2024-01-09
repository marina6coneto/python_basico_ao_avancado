import sys

#Generator expression, iterables e iterators em python
# O ITERÁVEL (ITERABLE) TEM A RESPONSABILIDADE DE TER O VALORES SEQUENCIALMENTE
# O ITERADOR (ITERATOR) TEM A RESPONSABILIDADE DE TE ENTREGAR UM VALOR POR VEZ (O PROXIMO VALOR)
# GENERATOR SÃO FUNÇÕES QUE SABEM PAUSAR EM DETERMINADAS OCASIÕES
iterable = ['Eu', 'Tenho', '__iter__']
iterator = iter(iterable) #tem __iter__ e __next__
lista = [n for n in range(10)]
generator = (n for n in range(10))

print(sys.getsizeof(lista))
print(sys.getsizeof(generator))
