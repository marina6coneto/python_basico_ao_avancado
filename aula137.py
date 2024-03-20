# Criando Exceptions em Python Orientado a Objetos
# Para criar uma Exception em Python, você só
# precisa herdar de alguma exceção da linguagem.
# A recomendação da doc é herdar de Exception.
# https://docs.python.org/3/library/exceptions.html
# Criando exceções (comum colocar Error ao final)
# Levantando (raise) / Lançando (throw) exceções
# Relançando exceções
# Adicionando notas em exceções (3.11.0# Levantando e tratando suas Exceptions (Exceções)
# Notas das exceptions em Python (add_notes, __notes__)

class MyError(Exception):
    ...

class OtherError(Exception):
    ...

def levantar():
    exception_ = MyError('A mensagem do meu erro.')
    exception_.add_note('Olha a nota 1')
    exception_.add_note('VC ERROU ISSO: ')
    raise exception_
try:
    levantar()
except (MyError, ZeroDivisionError) as error:
    print(error.__class__.__name__)
    print(error)
    print()
    exception_ = OtherError('Vou lançar outro erro')
    exception_.__notes__ = error.__notes__.copy()
    exception_.add_note('TERCEIRA NOTA')
    raise exception_ from error