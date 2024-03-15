# Exercício com classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem um Motor
# Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e um Fabricante
# Obs.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricante na tela


class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None
        
    @property
    def motor(self):
        return self._motor
    
    @motor.setter
    def motor(self, valor):
        self._motor = valor
        
    @property
    def fabricante(self):
        return self._fabricante
    
    @fabricante.setter
    def fabricante(self, valor):
        self._fabricante = valor
    
    
    
class Motor:
    def __init__(self, nome):
        self.nome = nome
    
    
class Fabricante:
    def __init__(self, nome):
        self.nome = nome
        
fusca = Carro('Fusca')
volkswagen = Fabricante('Volkswagen')
motor_1_0 = Motor('Motor 1.0')
fusca.fabricante = volkswagen
fusca.motor = motor_1_0
print(fusca.nome, fusca.fabricante.nome, fusca.motor.nome)

uno = Carro('Uno')
fiat = Fabricante('Fiat')
motor_1_4 = Motor('Motor 1.4')
uno.fabricante = fiat
uno.motor = motor_1_4
print(uno.nome, uno.fabricante.nome, uno.motor.nome)

up = Carro('Up')
up.fabricante = fiat
up.motor = motor_1_0
print(up.nome, up.fabricante.nome, up.motor.nome)