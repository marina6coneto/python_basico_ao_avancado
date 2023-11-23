"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""


lista = []

while True:
    print('Escolha uma opção abaixo, ou digite "sair" para sair do programa: ')
    opcao = str(input('[i]nserir  [a]pagar  [l]istar: '))
    
    if opcao == 'i':
        compras = input('Lista de compras: ')
        lista.append(compras)     
      
    elif opcao == 'a':
        indice_str = input('Escolha o índice para apagar: ')
        try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print('Por favor, digite número inteiro.')
        except IndexError:
            print('Índice não existe na lista.')
        except Exception:
            print('Erro desconhecido')
        
    elif opcao == 'l':
        if len(lista) == 0:
            print('Não há nada na lista.')
        for item, compras in enumerate(lista):
            print('Lista de compras: ')
            print(item, compras)
            
    elif opcao.lower().strip() == 'sair':
        break
          
    else:
        print('Essa não é uma opção válida.')
        print('Escolha entre [i], [a] ou [l]')
    



















