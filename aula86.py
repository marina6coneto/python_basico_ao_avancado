# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# https://brasilescola.uol.com.br/matematica/conjunto.htm
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.

# Criando um set
# set(iterável) ou {1, 2, 3}

# s1 = set('Luiz')
# s1 = set()  # vazio
# s1 = {'Luiz', 1, 2, 3}  # com dados
# print(s1)

# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - Não aceitam valores mutáveis; aceita tupla
# - Seus valores serão sempre únicos;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)

# l1 = [1, 2, 3, 3, 4, 3, 1]
# s1 = set(l1)
# l2 = list(s1)
# s1 = {1, 2, 3, 3, 3, 3, 3, 1}
#s1 = {1, 2, 3, (123,)}
#print(3 in s1)

# for numero in s1:
#     print(numero)

# Métodos úteis:
# add, update, clear, discard

# s1 = set()
# s1.add('Luiz')
# s1.add(1)
# s1.update(('Marina',))
#s1.clear()
# s1.discard('Luiz')
# print(s1)


# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos

s1 = {1, 2, 3}
s2 = {2, 3, 4}

s3 = s1 | s2
print(s3)

s4 = s1 & s2
print(s4)

s5 = s1 - s2 #ordem importa
print(s5)

s6 = s2 - s1 #ordem importa
print(s6)

s7 = s1 ^ s2
print(s7)