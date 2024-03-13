# Criando arquivos com Python + Context Manager with
# Usamos a função open para abrir
# um arquivo em Python (ele pode ou não existir)
# Modos:
# r (leitura), w (escrita), x (para criação)
# a (escreve ao final), b (binário)
# t (modo texto), + (leitura e escrita)
# Context manager - with (abre e fecha)
# Métodos úteis
# write, read (escrever e ler)
# writelines (escrever várias linhas)
# seek (move o cursor)
# readline (ler linha)
# readlines (ler linhas)
# Vamos falar mais sobre o módulo os, mas:
# os.remove ou unlink - apaga o arquivo
# os.rename - troca o nome ou move o arquivo
# Vamos falar mais sobre o módulo json, mas:
# json.dump = Gera um arquivo json
# json.load
import os

caminho_arquivo = 'C:\\Users\\santo\\OneDrive\\Área de Trabalho\\Python 3 do Básico ao Avançado\\python arquivo\\'
caminho_arquivo += 'aula106.txt'

# arquivo = open(caminho_arquivo, 'w')

# arquivo.close()

# with open(caminho_arquivo, 'w+') as arquivo:
#     print(type(arquivo))
#     arquivo.write('O meu time é o Avaí\n')
#     arquivo.write('Eu gosto de Harry Potter\n')
#     arquivo.writelines(
#         ('Sou estudante\n', 'Sou estagiária\n')
#     )
#     arquivo.seek(0,0)
#     print(arquivo.read())
#     print('Lendo\n')
#     arquivo.seek(0,0)
#     print(arquivo.readline(), end='')
#     print(arquivo.readline().strip())
#     print(arquivo.readline(), end='')
#     print(arquivo.readline())
#     print('READLINES\n')
#     arquivo.seek(0,0)
#     for linha in arquivo.readlines():
#         print(linha.strip())

with open(caminho_arquivo, 'a+', encoding='utf8') as arquivo:
    arquivo.write('atenção\n')
    arquivo.write('linha 1\n')
    arquivo.write('linha 2\n')
    
