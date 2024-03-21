# Context Manager com função - Criando e Usando gerenciadores de contexto
from contextlib import contextmanager

@contextmanager
def my_open(caminho_arquivo, modo):
    try:
        print('Abrindo Arquivo...')
        arquivo = open(caminho_arquivo, modo, encoding='utf8')
        yield arquivo
    except Exception as e:
        print('Ocorreu erro: ', e)
    finally:
        print('Fechando Arquivo...')
        arquivo.close()


with my_open('aula142.txt', 'w') as arquivo:
    arquivo.write('Avaí\n')
    arquivo.write('Alimentando o TXT\n', 123)
    arquivo.write('Marina\n')
    print('WITH', arquivo)