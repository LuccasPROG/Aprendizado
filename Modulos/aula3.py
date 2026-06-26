# datetime.timedelta e dateutil.relativetimedelta (calculando datas)
# Docs:
# https://dateutil.readthedocs.io/en/stable/relativedelta.html
# https://docs.python.org/3/library/datetime.html#timedelta-objects

from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

fmt = '%d/%m/%Y %H:%M:%S'
data_inicio = datetime.strptime('20/04/1987 09:30:30', fmt)
data_Fim = datetime.strptime('12/12/2026 15:59:59', fmt)

delta = relativedelta(data_Fim, data_inicio)
print(delta)
print(data_Fim)
print(data_Fim + relativedelta(second=59, minutes=10))


# print(data_Fim - data_inicio)
# print(data_Fim > data_inicio)


