from datetime import datetime 
from pytz import timezone

'''
https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
'''

# print(datetime.now(timezone('Asia/Tokyo')))

data = datetime.now()
# print(datetime.now().timestamp())

data_ = data.fromtimestamp(1677408505)
print(data_)
