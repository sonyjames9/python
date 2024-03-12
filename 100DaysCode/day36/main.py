import requests
from twilio.rest import Client
import os

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "3JGS4523DXDQS477"
NEWS_API_KEY = "1c8046ab438c4443955306431c6ee218"

TWILIO_SID = os.environ.get("TWILIO_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
# print(response.json())

data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
print(yesterday_closing_price)

day_before_yest = data_list[1]
day_before_yest_closing_price = day_before_yest["4. close"]
print(day_before_yest_closing_price)

diff = float(yesterday_closing_price) - float(day_before_yest_closing_price)
print(diff)


diff_percent = diff/float(yesterday_closing_price) *100

print(f"diff_percent : {diff_percent}")

abs_diff = abs(diff_percent)
abs_diff = round(abs_diff, 2)
if float(abs_diff) > 2:
    # print("Get News : ")

    news_params = {
        "apiKey": "1c8046ab438c4443955306431c6ee218",
        "q": COMPANY_NAME

    }
    if float(abs_diff) > 2:
        up_down = "🔺"
    else:
        up_down = "🔻"
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]
    first_three_news = articles[:3]
    # print(first_three_news)

    formatted_articles = [(f"{STOCK_NAME}: {up_down}{abs_diff}%'\n'Headline: {article['title']}, Url:"
                           f" {article['url']}") for
                          article
                          in
                          first_three_news]
    print(formatted_articles)

    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_='+13235534389',
            to='+917276365937'
        )
        print(message.sid)
        print(message.status)




