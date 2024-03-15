# Relações entre classes: associação, agregação e composição
# Composição é uma especialização da agregação.
# Mas nela, quando o objeto "pai" for apagado, todas
# as referências dos objetos filhos também são
# apagadas.

class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.enderecos = []
        
    def inserir_endereco(self, rua, numero):
        self.enderecos.append(Endereco(rua, numero))    
        
    def listar_endereco(self):
        for endereco in self.enderecos:
            print(endereco.rua, endereco.numero)
            
    def __del__(self):
        print('Apagando...', self.nome)
        
        
class Endereco:
    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero
    
    def __del__(self):
        print('Apagando', self.rua, self.numero)
        
        
cliente = Cliente('Marina')   
print(cliente.nome)
cliente.inserir_endereco('Edeling Schutz', 58)
cliente.listar_endereco()     

