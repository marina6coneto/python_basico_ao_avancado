# sys.argv - Executando arquivos com argumentos no sistema
# Fonte = Fira Code
import sys


argumento = sys.argv
qntd_argumento = len(argumento)
print(qntd_argumento)

if qntd_argumento <= 1:
    print('Você não passou argumentos')
else:
    try:
        print(f'Voce Passou os argumentos {argumento[1:]}')
        print(f'Faça alguma coisa com {argumento[1:]}')
        print(f'Faça outra coisa com {argumento[2:]}')
    except IndexError:
        print('Faltam argumentos')