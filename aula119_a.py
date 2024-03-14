# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.
import json 

CAMINHO_ARQUIVO = 'aula119.json'

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
        
p1 = Pessoa('Marina', 25)
p2 = Pessoa('Felipe', 23)
p3 = Pessoa('Harry', 30)

bd = [vars(p1), p2.__dict__, vars(p3)]

def fazer_dump():
    with open(CAMINHO_ARQUIVO, 'w') as arquivo:
        json.dump(bd, arquivo, ensure_ascii=False, indent=2)
        
if __name__ == '__main__':
    print('ELE É O __main__')
    fazer_dump()