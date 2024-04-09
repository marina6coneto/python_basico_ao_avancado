# string.Template para substituir variáveis em textos
# doc: https://docs.python.org/3/library/string.html#template-strings
# Métodos:
# substitute: substitui mas gera erros se faltar chaves
# safe_substitute: substitui sem gerar erros
# Você também pode trocar o delimitador e outras coisas criando uma subclasse
# de template.
import locale
import string
from datetime import datetime
from pathlib import Path

CAMINHO_ARQUIVO = Path(__file__).parent / 'aula182.txt'


locale.setlocale(locale.LC_ALL, '')

def converte_para_brl(numero: float | int) -> str:
    brl = 'R$ ' + locale.currency(val=numero, symbol=False, grouping=True)
    return brl

data = datetime(1998, 6, 5)
dados = dict(
    nome = 'Marina',
    valor = converte_para_brl(1_234_456),
    data = data.strftime('%d/%m/%Y' ),
    empresa = 'N.V.',
    telefone = '+55 (48) 3242-6863'
)

class MyTemplate(string.Template):
    delimiter = '%'

with open(CAMINHO_ARQUIVO, 'r', encoding='utf8') as arquivo:
    texto = arquivo.read()
    template = MyTemplate(texto)
    print(template.substitute(dados))




