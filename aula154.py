from dataclasses import dataclass

@dataclass
class Pessoa:
    nome: str
    sobrenome: str
    
    @property
    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'
    
    @nome_completo.setter
    def nome_completo(self, valor):
        nome, *sobrenome = valor.split()
        self.nome = nome
        self.sobrenome = ' '.join(sobrenome)
    
if __name__ == '__main__':
    p1 = Pessoa('Marina', 'Cesconeto')
    print(p1)
    print(p1.nome_completo)
    p1.nome_completo = 'Felipe Leite de Sousa'
    print(p1.nome_completo)