#Nama
# first_name = 'Joseph'
# last_name = 'Choi'
# full_name = f'{first_name} {last_name}'
# print(full_name)

#Datetime
# from datetime import datetime

# today = datetime.now()
# print(today)

#Datetime terbaru
from datetime import datetime

today = datetime.now()

date_time = today.strftime('%Y-%m-%d-%H-%M-%S')

print(date_time)