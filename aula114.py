# Entendendo self em classes Python
# Classe - Molde (geralmente sem dados)
# Instância da class (objeto) - Tem os dados
# Uma classe pode gerar várias instâncias.
# Na classe o self é a própria instância.

class Carro:
    def __init__(self, nome):
        self.nome = nome
        
    def acelerar(self):
        print(f'O {self.nome} está acelerando...')
        

fusca = Carro('Fusca')
print(fusca.nome)
# fusca.acelerar() 
# OU PODE SER FEITO PELO CÓDIGO ABAIXO
Carro.acelerar(fusca)

celta = Carro('Celta')
print(celta.nome)
# celta.acelerar()
# OU PODE SER FEITO PELO CÓDIGO ABAIXO
Carro.acelerar(celta)