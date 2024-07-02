import requests
from datetime import datetime
import time

from_date = input('Enter start date in dd/mm/yyyy format : ')
to_date = input('Enter end date in dd/mm/yyyy format : ')

url = "https://query1.finance.yahoo.com/v7/finance/download/AAPL?period1=34542700&period2=1642032000&interval=1d&events=history&includeAdjustedClose=true"
headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"}


from_datime = datetime.strptime(from_date, 'm%/%d/%Y')
to_datetime = datetime.strptime(to_date, 'm%/%d/%Y')

content = requests.get(url, headers=headers).content
print(content)

with open('data.csv', 'wb') as file:
    file.write(content)