# Criando datas com módulo datetime
# datetime(ano, mês, dia)
# datetime(ano, mês, dia, horas, minutos, segundos)
# datetime.strptime('DATA', 'FORMATO')
# datetime.now()
# https://pt.wikipedia.org/wiki/Era_Unix
# datetime.fromtimestamp(Unix Timestamp)
# https://docs.python.org/3/library/datetime.html
# Para timezones
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
# Instalando o pytz
# pip install pytz types-pytz

from datetime import datetime


data = datetime.now()
print(data.timestamp())
print(datetime.fromtimestamp(1711484586.932868))

# from pytz import timezone

# date = datetime.now()

# data_str_data = '2024-03-26 16:06:26'
# data_str_fmt = '%Y-%m-%d %H:%M:%S'
# date = datetime(2024, 3, 26, 16, 6, 26, tzinfo=timezone('Asia/Tokyo'))

# print(date)