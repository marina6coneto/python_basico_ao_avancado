# Yield from
def gen1():
    yield 1
    yield 2
    yield 3

def gen3():
    yield 10
    yield 20
    yield 30

def gen2(gen=None):
    if gen is not None:
        yield from gen
    yield 4
    yield 5
    yield 6


g1 = gen1()
g2 = gen2()
g3 = gen2()
for numero in g1:
    print(numero)
print()
for numero in g2:
    print(numero)
print()
for numero in g3:
    print(numero)
print()