# datetime.timedelta e dateutil.relativetimedelta (calculando datas)
# Docs:
# https://dateutil.readthedocs.io/en/stable/relativedelta.html
# https://docs.python.org/3/library/datetime.html#timedelta-objects

from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta


fmt = '%d/%m/%Y %H:%M:%S'
data_inicio = datetime.strptime('05/06/1998 19:22:00', fmt)
data_fim = datetime.strptime('26/03/2024 21:29:32', fmt)
#delta = timedelta(days=10, hours=3)
delta = relativedelta(data_fim, data_inicio)
print(delta.days, delta.years)

# print(data_fim + delta)
# print(data_fim + relativedelta(seconds=59))
#delta = data_fim - data_inicio
# print(data_fim < data_inicio)
# print(data_fim > data_inicio)
# print(data_fim == data_inicio)
# print(delta.days, delta.seconds, delta.microseconds)
# print(delta.total_seconds())