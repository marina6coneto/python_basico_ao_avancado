# Exercício - sistema de perguntas e respostas

perguntas = [
    {
        'Pergunta': 'Qual o ano que o Avaí foi fundado?',
        'Opções': ['1920', '1921', '1922', '1923'],
        'Resposta': '1923',
    },
    {
        'Pergunta': 'Qual o mascote do Avaí?',
        'Opções': ['Macaco', 'Leão', 'Gavião', 'Urubu'],
        'Resposta': 'Leão',
    },
    {
        'Pergunta': 'Qual o maior time de futebol de SC?',
        'Opções': ['Figueirense', 'Chapecoense', 'Avaí', 'Cricíuma'],
        'Resposta': 'Avaí',
    },
]

qtd_acertos = 0
for dicionario in perguntas:
    print('Pergunta:',dicionario['Pergunta'])
    print()
    
    opcoes = dicionario['Opções']
    for i, opcao in enumerate(opcoes):
        print(f'{i})',opcao)
    print()
        
    escolha  = input('Escolha uma opção: ')
    
    acertou = False
    escolha_int = None
    qtd_opcoes = len(opcoes)

    if escolha.isdigit():
        escolha_int = int(escolha)

    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int < qtd_opcoes:
            if opcoes[escolha_int] == dicionario['Resposta']:
                acertou = True

    print()
    if acertou:
        qtd_acertos += 1
        print('Acertou 👍')
    else:
        print('Errou ❌')

    print()


print(f'Você acertou {qtd_acertos} de {len(dicionario)} perguntas')
   
    
    