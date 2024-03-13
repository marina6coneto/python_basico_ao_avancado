# class - Classes são moldes para criar novos objetos
# As classes geram novos objetos (instâncias) que
# podem ter seus próprios atributos e métodos.
# Os objetos gerados pela classe podem usar seus dados
# internos para realizar várias ações.
# Por convenção, usamos PascalCase para nomes de
# classes.

# string = 'marina'
# print(string.upper())
# print(isinstance(string, str))
class Pessoa:
    ...
    
p1 = Pessoa()
p1.nome = 'Marina'
p1.sobrenome = 'Cesconeto'
print(p1.nome)
print(p1.sobrenome)

p2 = Pessoa()
p2.nome = 'Felipe'
p2.sobrenome = 'Leite'
print(p2.nome)
print(p2.sobrenome)

