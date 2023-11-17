""" Calculadora com 
      WHILE!!!!!!!!!
"""

while True:
      n1 = float(input('Digite um número: '))
      n2 = float(input('Digite outro número: '))
      operador = input('Digite o operador (+)(-)(*)(/): ')
      
      operadores_permitidos = '+-*/'
      if operador not in operadores_permitidos:
            print('Operador inválido.')
            continue
      if len(operador) > 1:
            print('Digite um operador.')
            continue
      print('Realizando sua conta. Confira o resultado abaixo:')
      if operador == '+':
            n3 = n1 + n2
            print(f'Resultado: {n3:.2f}')
      elif operador == '-':
            n3 = n1 - n2
            print(f'Resultado: {n3:.2f}')
      elif operador == '*':
            n3 = n1 * n2
            print(f'Resultado: {n3:.2f}')
      elif operador == '/':
            n3 = n1 / n2
            print(f'Resultado: {n3:.2f}')
      
      sair = input('Quer sair? [s]im ').lower().strip().startswith('s')
      if sair is True:
            break