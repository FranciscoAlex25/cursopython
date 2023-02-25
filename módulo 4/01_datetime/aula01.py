from datetime import datetime

data_str = '25/02/2023'
data_format = '%d/%m/%Y'

# data = datetime(2023, 2, 25, 10, 40)

print(datetime.strptime(data_str, data_format))
