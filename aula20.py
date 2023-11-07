#Exercício
primeiro_valor = int(input('Digite um valor: '))
segundo_valor = int(input('Digite outro valor: '))
if primeiro_valor > segundo_valor:
    print(f'{primeiro_valor=} é maior que o {segundo_valor=}.')
elif segundo_valor > primeiro_valor:
    print(f'{segundo_valor=} é maior que o {primeiro_valor=}.')
else:
    print('Os valores são iguais.')