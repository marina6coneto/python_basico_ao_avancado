# Atributos de Classe
class Pessoa:
    ano_atual = 2024
    
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade
    
    
p1 = Pessoa('Felipe', 23)
p2 = Pessoa('Marina', 25)


print(Pessoa.ano_atual)
print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())