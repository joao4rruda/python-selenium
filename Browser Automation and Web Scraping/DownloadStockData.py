import requests
from datetime import datetime
import time

try:
    ticker = input("Enter the ticker symbol: ")
    from_date = input('Enter start date in dd/mm/yyyy format: ')
    to_date = input('Enter end date in dd/mm/yyyy format: ')

    from_datetime = datetime.strptime(from_date, '%Y/%m/%d')
    to_datetime = datetime.strptime(to_date, '%Y/%m/%d')

    from_epoch = int(time.mktime(from_datetime.timetuple()))
    to_epoch = int(time.mktime(to_datetime.timetuple()))

    url = f"https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={from_epoch}&period2={to_epoch}&interval=1d&events=history&includeAdjustedClose=true"
    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"}

    response = requests.get(url, headers=headers)
    content = response.content.decode('utf-8')
    print(content)

    with open('data.csv', 'wb') as file:
        file.write(response.content)

    print("Data saved to 'data.csv'")

except Exception as e:
    print(f"An error occurred: {e}")
