
#Generator expression, iterables e iterators em python
# O ITERÁVEL (ITERABLE) TEM A RESPONSABILIDADE DE TER O VALORES SEQUENCIALMENTE
# O ITERADOR (ITERATOR) TEM A RESPONSABILIDADE DE TE ENTREGAR UM VALOR POR VEZ (O PROXIMO VALOR)

iterable = ['Eu', 'Tenho', '__iter__']
iterator = iter(iterable) #tem __iter__ e __next__


print(next(iterator))
print(next(iterator))
print(next(iterator))