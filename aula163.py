# Formatando datas do datetime
# datetime.strftime('DATA', 'FORMATO')
# https://docs.python.org/3/library/datetime.html


from datetime import datetime


fmt = '%d/%m/%Y'

#data = datetime(2024, 3, 26, 18, 1, 25)
data = datetime.strptime('2024-03-26 18:03:58', '%Y-%m-%d %H:%M:%S')
print(data.strftime(fmt))
print(data.strftime('%d/%m/%Y %H:%M'))
print(data.strftime('%d/%m/%Y %H:%M:%S'))
print(data.strftime('%Y'), data.year)
print(data.strftime('%d'), data.day)
print(data.strftime('%m'), data.month)
print(data.strftime('%H'), data.hour)
print(data.strftime('%M'), data.minute)
print(data.strftime('%S'), data.second)