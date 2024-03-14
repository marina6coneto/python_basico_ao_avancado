# __dict__ e vars para atributos de instância
class Pessoa:
    ano_atual = 2024
    
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade
    


dados = {'nome': 'Felipe', 'idade': 23}
p1 = Pessoa(**dados)

print(vars(p1))
print(p1.nome)