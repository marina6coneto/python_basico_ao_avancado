from dataclasses import dataclass


@dataclass(init=False)
@dataclass(repr=True)
class Pessoa:
    nome: str
    sobrenome: str

    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
        self.nome_completo = f'{self.nome} {self.sobrenome}'

    def __post_init__(self):
        print('POST INIT')

    # @property
    # def nome_completo(self):
    #     return f'{self.nome} {self.sobrenome}'

    # @nome_completo.setter
    # def nome_completo(self, valor):
    #     nome, *sobrenome = valor.split()
    #     self.nome = nome
    #     self.sobrenome = ' '.join(sobrenome)


if __name__ == '__main__':
    p1 = Pessoa('Marina', 'Cesconeto')
    print(p1)
    print(p1.nome_completo)
    lista = [Pessoa('Amanda', 'Zena'), Pessoa('Beatriz', 'Yield'), Pessoa('Carolina', 'Xima')]
    ordenadas = sorted(lista, reverse=True, key=lambda p: p.sobrenome)
    print(ordenadas)