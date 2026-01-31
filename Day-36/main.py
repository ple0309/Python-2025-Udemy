from newsapi import NewsApiClient

# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
import requests
from datetime import date, timedelta

# # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=V98VM7QX0HD2SA5A'

r = requests.get(url)
data = r.json()
print(data)

today = date.today()
yesterday = today - timedelta(days=1)
day_before_yesterday = today - timedelta(days=2)
#
# today = today.isoformat()
yesterday = yesterday.isoformat()
day_before_yesterday = day_before_yesterday.isoformat()
print(yesterday)
print(day_before_yesterday)

price_yesterday = float(data["Time Series (Daily)"][yesterday]["1. open"])
price_day_before_yesterday = float(data["Time Series (Daily)"][day_before_yesterday]["4. close"])

print(price_yesterday)
print(price_day_before_yesterday)

percentage = "TSLA: "
if (price_yesterday -  price_day_before_yesterday) < 0:
    percentage += "🔻"
else:
    percentage += "🔺"
ratio = (abs(price_yesterday - price_day_before_yesterday) * 100) / price_yesterday
difference = str(ratio)
percentage += difference


parameters = {
    'q':'TSLA',
    'from': f'{yesterday}',
    'publishedAt': f'{yesterday}',
    'sortBy':"popularity",
    'apiKey': 'f06f698f835b44e0be9c3e5167c719ee'
}
url = 'https://newsapi.org/v2/everything'

response = requests.get(url, params=parameters)
data = response.json()
head_line = data["articles"][0]['title']
brief = data["articles"][0]['description']

description = f"{percentage}\n{head_line}\n{brief}" if ratio > 5 else f"{head_line}\n{brief}"
print(description)




