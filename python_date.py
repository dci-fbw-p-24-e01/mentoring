import datetime as dt

now = dt.datetime.now()

# print(now)
# print(type(now))

birthday = dt.datetime(2024, 4, 22, 10, 33, 44)

# print(birthday)

now_to_future = now + dt.timedelta(5)

# print(now_to_future)

formatted_date = now.strftime('Date: %Y/%m/%d \nTime: %H:%M:%S')

# print(formatted_date)

music_concert = 'The music concert will take place on 15th of August 2024 at 20:30 o\'clock.'

music_date = dt.datetime.strptime(music_concert, 'The music concert will take place on %dth of %B %Y at %H:%M o\'clock.')

# print(music_date)


import pytz

utc = pytz.utc

indian_time = pytz.timezone('Asia/Kolkata')


utc_time = dt.datetime.now(utc)

kolkata_time = utc_time.astimezone(indian_time)

# print(now)
# print(utc_time)
# print(kolkata_time)


# Create datetime using numpy

import numpy as np


numpy_date = np.datetime64('2024-10-22T14:30:40')

# print(numpy_date)
# print(type(numpy_date))

june_dates = np.arange('2024-06-01', '2024-07-01', dtype='datetime64')

# print(june_dates)


import pandas as pd

pandas_date = pd.Timestamp('2024-11-28T16:33:55')

# print(pandas_date)
# print(pandas_date.year)
# print(pandas_date.month)
# print(pandas_date.day)

py_date = pandas_date.to_pydatetime()

# print(py_date)
# print(type(py_date))

