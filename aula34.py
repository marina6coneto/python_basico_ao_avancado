
"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
hora_str = input('Digite a hora em números inteiros:')

try:
    hora_int = int(hora_str)
    if hora_int >= 0 and hora_int <= 11:
        print(f'Bom dia, é {hora_int} horas.')
    elif hora_int >= 12 and hora_int <=17:
        print(f'Boa tarde, é {hora_int} horas.')
    elif hora_int >= 18 and hora_int <=23:
        print(f'Boa noite, é {hora_int} horas.')
    else:
        print('Não conheço essa hora.')
        
except:
    print(f'Essa hora, {hora_str}, não esta em números inteiros.')

