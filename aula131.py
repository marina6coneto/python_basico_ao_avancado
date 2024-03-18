# super() e a sobreposição de membros - Python Orientado a Objetos
# Classe principal (Pessoa)
#   -> super class, base class, parent class
# Classes filhas (Cliente)
#   -> sub class, child class, derived class
# class MinhaString(str):
#    def upper(self):
#        print('CHAMOU UPPER')
#        retorno = super(MinhaString, self).upper()
#        print('DEPOIS DO UPPER')
#        return retorno

# string = MinhaString('Marina')
# print(string.upper())

class A:
    
    atributo_a = 'Valor a'
    
    def __init__(self, atributo):
        self.atributo = atributo
        
    
    def metodo(self):
        print('A')
        
class B(A):
    
    atributo_b = 'Valor b'
    
    def __init__(self, atributo, outra_coisa):
        super().__init__(atributo)
        self.outra_coisa = outra_coisa
    
    def metodo(self):
        print('B')
        
class C(B):
    
    atributo_c = 'Valor c'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print('BURLEI O SISTEMAAAAA!')
    
    def metodo(self):
        #super().metodo() #B
        #super(B, self).metodo() #C
        A.metodo(self)
        B.metodo(self)
        
        
        
c = C('Atributo', 'Outra Coisa')
print(c.atributo, c.outra_coisa)
print(c.atributo_a)
print(c.atributo_b)
print(c.atributo_c)
c.metodo()

print(C.mro())
print(B.mro())
print(A.mro())