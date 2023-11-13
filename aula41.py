"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""
qnt_linhas = 5
qnt_colunas = 5
linha = 1
while linha <= qnt_linhas:
    coluna  = 1
       
    while coluna <= qnt_colunas:
        print(f'{linha=} {coluna=}')
        coluna +=1
    linha +=1
print('Acabou')