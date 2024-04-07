# csv.writer e csv.DictWriter para escrever em CSV
# csv.reader lê o CSV em formato de lista
# csv.DictReader lê o CSV em formato de dicionário

import csv
from pathlib import Path

CAMINHO_CSV = Path(__file__).parent / 'aula179.csv'

lista_clientes = [
     {'Nome': 'Marina', 'Endereco': 'Palhoça'},
     {'Nome': 'Felipe', 'Endereco': 'Florianópolis'},
     {'Nome': 'Marquinhos', 'Endereco': 'Biguaçu'}
 ]

with open(CAMINHO_CSV, 'w') as arquivo:
    nome_colunas = lista_clientes[0].keys()
    escritor = csv.DictWriter(
        arquivo,
        fieldnames=nome_colunas
    )
    escritor.writeheader()

    for clientes in lista_clientes:
        escritor.writerow(clientes)


# lista_clientes = [
#     ['Marina', 'Palhoça'],
#     ['Felipe', 'Florianópolis'],
#     ['Marquinhos', 'Biguaçu']
# ]

# with open(CAMINHO_CSV, 'w') as arquivo:
#     # nome_colunas = lista_clientes[0].keys()
#     nome_colunas = ['Nome', 'Endereço']
#     escritor = csv.writer(arquivo)
#     escritor.writerow(nome_colunas)
    
#     for clientes in lista_clientes:
#         escritor.writerow(clientes)