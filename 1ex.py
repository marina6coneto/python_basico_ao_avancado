def cria_multiplicador(multiplicador):
    def multiplica(numero):
        return multiplicador * numero
    return multiplica

numero = int(input('Digite o número que queira multiplicar: '))
multiplicador = int(input('Digite o multiplicador: '))

funcao_multiplicadora = cria_multiplicador(multiplicador)

resultado = funcao_multiplicadora(numero)

print(f"O resultado da multiplicação é: {resultado}")