# Encapsulamento (modificadores de acesso: public, protected, private)
# Python NÃO TEM modificadores de acesso
# Mas podemos seguir as seguintes convenções
#   (sem underline) = public
#       pode ser usado em qualquer lugar
# _ (um underline) = protected
#       não DEVE ser usado fora da classe
#       ou suas subclasses.
# __ (dois underlines) = private
#       "name mangling" (desfiguração de nomes) em Python
#       _NomeClasse__nome_attr_ou_method
#       só DEVE ser usado na classe em que foi
#       declarado.

from functools import partial

class Foo:
    def __init__(self):
        self.public = 'isso é público'
        self._protected = 'isso é protegido'
        self.__private = 'Isso é privado'
        
    def metodo_publico(self):
        print(self.__private)
        self.__metodo_private()
        return 'método público'
        
    
    def _metodo_protegido(self):
        return '_Método Protegido'

    def __metodo_private(self):
        print('MÉTODO PRIVADO')
        return 'privado'
        
f = Foo()
print(f.public)
print(f.metodo_publico())
print(f._protected) #não é uma boa pratica em python pois está fora da classe
print(f._metodo_protegido()) #não é uma boa pratica em python pois está fora da classe
