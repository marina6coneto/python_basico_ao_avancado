# Relações entre classes: associação, agregação e composição
# Agregação é uma forma mais especializada de associação
# entre dois ou mais objetos. Cada objeto terá
# seu ciclo de vida independente.
# Geralmente é uma relação de um para muitos, onde um
# objeto tem um ou muitos objetos.
# Os objetos podem viver separadamente, mas pode
# se tratar de uma relação onde um objeto precisa de
# outro para fazer determinada tarefa.
# (existem controvérsias sobre as definições de agregação).

class Carrinho:
    def __init__(self):
        self._produtos = []
        
    def total(self):
        return sum([p.preco for p in self._produtos])
    
    def inserir_produto(self, *produtos):
        self._produtos.extend(produtos)
    
    def listar_produtos(self):
        print()
        for produto in self._produtos:
            print(produto.nome, produto.preco)
        print()
        
        
class Produtos:
    
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
        
carrinho = Carrinho()
p1, p2 = Produtos('Camisa', 300), Produtos('Short', 199)
carrinho.inserir_produto(p1, p2)
carrinho.listar_produtos()
print(carrinho.total())