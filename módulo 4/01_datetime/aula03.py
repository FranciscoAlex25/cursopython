from datetime import datetime

data1 = '%d/%m/%Y'


data1_formatada = datetime.strptime('23/03/2000', data1)
data2_formatada = datetime.strptime('12/04/1998', data1)

print(data1_formatada < data2_formatada)
print(data1_formatada == data2_formatada)
