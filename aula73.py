"""
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e local.
O escopo global é o escopo onde todo o código é alcançavel.
O escopo local é o escopo onde apenas nomes do mesmo local
podem ser alcançados.
Não temos acesso a nomes de escopos internos nos escopos externos.
A palavra global faz uma variável do escopo externo ser a mesma no escopo interno.
"""
x = 34
def escopo():
    global x #alterando variáveis de escopo externo em escopo interno mas é MÁ PRÁTICA!!
    x = 10
    def outra_funcao():
        x = 97
        y = 2
        print(x, y)
    outra_funcao()
    print(x)
print(x)  
escopo()
print(x)

