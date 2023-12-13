# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.
# esse exercício tem 3 funções

def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar  

duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

numero_multiplicar = int(input('Qual número você deseja multiplicar por 2, 3 e 4? '))

print(f'O número {numero_multiplicar} foi multiplicado e o resultado foi: {duplicar(numero_multiplicar)}')
print(f'O número {numero_multiplicar} foi multiplicado e o resultado foi: {triplicar(numero_multiplicar)}')
print(f'O número {numero_multiplicar} foi multiplicado e o resultado foi: {quadruplicar(numero_multiplicar)}')