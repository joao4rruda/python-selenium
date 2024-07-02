import requests
from datetime import datetime
import time

from_date = input('Enter start date in dd/mm/yyyy format : ')
to_date = input('Enter end date in dd/mm/yyyy format : ')


from_datime = datetime.strptime(from_date, 'Y%/%m/%d')
to_datetime = datetime.strptime(to_date, 'Y%/%m/%d')

from_epoch = time.mktime(from_datime.timetuple())
to_epoch = time.mktime(to_datetime.timetuple())

url = f"https://query1.finance.yahoo.com/v7/finance/download/AAPL?period1={from_epoch}&period2={to_epoch}&interval=1d&events=history&includeAdjustedClose=true"
headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"}

content = requests.get(url, headers=headers).content
print(content)

with open('data.csv', 'wb') as file:
    file.write(content)