# dataclasses - O que são dataclasses?
# O módulo dataclasses fornece um decorador e funções para criar métodos como
# __init__(), __repr__(), __eq__() (entre outros) em classes definidas pelo
# usuário.
# Em resumo: dataclasses são syntax sugar para criar classes normais.
# Foi descrito na PEP 557 e adicionado na versão 3.7 do Python.
# doc: https://docs.python.org/3/library/dataclasses.html

from dataclasses import dataclass

@dataclass
class Pessoa:
    nome: str
    idade: int
    
    
if __name__ == '__main__':
    p1 = Pessoa('Marina', 25)
    p2 = Pessoa('Felipe', 23)
    print(p1)
    print(p2)
    print(p1 == p2)
    p3 = Pessoa('Marina', 25)
    p4 = Pessoa('Marina', 25)
    print(p3 == p4)