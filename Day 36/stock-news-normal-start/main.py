import requests

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla"

STOCK_ENDPOINT = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=APIKEY"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

response = requests.get(url=STOCK_ENDPOINT)
data = response.json()
last_refreshed = data["Meta Data"]["3. Last Refreshed"]
yesterdays_close = float(data["Time Series (Daily)"][last_refreshed]["4. close"])

ereyesterday = f"{((last_refreshed.split("-"))[0])}-{((last_refreshed.split("-"))[1])}-0{str((int(last_refreshed.split("-")[2])) - 1)}"
ereyesterdays_close = float(data["Time Series (Daily)"][ereyesterday]["4. close"])

positive_difference = abs(yesterdays_close-ereyesterdays_close)

average_close = (ereyesterdays_close + yesterdays_close) / 2.0
percentage_difference = round((positive_difference / average_close) * 100)

if percentage_difference >= 5:
    news_api = f"https://newsapi.org/v2/everything?q={COMPANY_NAME}&from={last_refreshed}&sortBy=popularity&apiKey=APIKEY"
    response_news = requests.get(news_api)
    article_data = response_news.json()
    first_three_articles = article_data['articles'][3::]
    x = -1
    for article in range(3):
        x += 1
        print(f"{COMPANY_NAME} Stock: %{percentage_difference} change!")
        print(first_three_articles[x]["title"])
        print(first_three_articles[x]["description"])
        print(first_three_articles[x]["content"])
