# os.listdir para navegar em caminhos
#C:\Users\santo\Pictures\Capturas de Tela
# caminho = r'C:\\Users\\santo\\Pictures\\Capturas de Tela'
# print(caminho)

import os

caminho = os.path.join('/Users', 'santo', 'Pictures')

for pasta in os.listdir(caminho):
    caminho_completo_pasta = os.path.join(caminho, pasta)
    print(pasta)

    if not os.path.isdir(caminho_completo_pasta):
        continue

    for imagem in os.listdir(caminho_completo_pasta):
        print('  ', imagem)