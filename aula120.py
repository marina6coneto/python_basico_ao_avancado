# Métodos de classe + factories (fábricas)
# São métodos onde "self" será "cls", ou seja,
# ao invés de receber a instância no primeiro
# parâmetro, receberemos a própria classe.

class Pessoa:
    ano = 2024   #atributo de classe
        
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    @classmethod
    def metodo_de_classe(cls):
        print('Hey')
        
    @classmethod
    def criar_50_anos(cls, nome):
        return cls(nome, 50)
        
    @classmethod
    def criar_anonima(cls, idade):
        return cls('Anônimo(a)', idade)
    
        
p1 = Pessoa('Marina', 25)
p2 = Pessoa.criar_50_anos('Felipe')
p3 = Pessoa.criar_anonima(23)
print(p2.nome, p2.idade)
print(p3.nome, p3.idade)
#Pessoa.metodo_de_classe()