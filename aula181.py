# secrets gera números aleatórios seguros
#python -c "import string as s;from secrets import SystemRandom as Sr; print(''.join(Sr().choices(s.ascii_letters + s.punctuation + s.digits,k=12)))" COMANDO PARA GERAR UMA SENHA 
import secrets
import string as s 
from secrets import SystemRandom as Sr

random = secrets.SystemRandom()

print(''.join(Sr().choices(s.ascii_letters + s.digits + s.punctuation, k=12)))

# print(secrets.randbelow(100))
# print(secrets.choice([100, 32, 45]))

# random.randrange(início, fim, passo)
#   -> Gera um número inteiro aleatório dentro de um intervalo específico
r_range = random.randrange(10,20, 2)
# print(r_range)

# random.randint(início, fim)
#   -> Gera um número inteiro aleatório dentro de um intervalo "sem passo"
r_int = random.randint(10,20)
# print(r_int)

# random.uniform(início, fim)
#   -> Gera um número flutuante aleatório dentro de um intervalo "sem passo"
r_uniform = random.uniform(10,20)
# print(r_uniform)

# random.shuffle(SequenciaMutável) -> Embaralha a lista original
nomes = ['Felipe', 'Marina', 'Valeria', 'Nazareno']
#random.shuffle(nomes)
# print(nomes)

# random.sample(Iterável, k=N)
#   -> Escolhe elementos do iterável e retorna outro iterável (não repete)
novos_nomes = random.sample(nomes, k=2) #tbm embaralha
# print(nomes)
# print(novos_nomes)

# random.choices(Iterável, k=N)
#   -> Escolhe elementos do iterável e retorna outro iterável (repete valores)
novos_nomes = random.choices(nomes, k=3)
#print(novos_nomes)

# random.choice(Iterável) -> Escolhe um elemento do iterável
# print(random.choice(nomes))


