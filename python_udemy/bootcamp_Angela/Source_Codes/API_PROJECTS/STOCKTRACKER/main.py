import requests
from datetime import datetime, timedelta
from twilio.rest import Client

now = datetime.now()
now = now.date()
yesterday = str(now - timedelta(days = 1))
before_yesterday = str(now - timedelta(days = 2))
print(yesterday)
print(before_yesterday)

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API_KEY = "1XFJ9WQW3KRQOUFU"
NEWS_API_KEY = "f3ca7ffbf6294c20bd64db7ba5ff8d04"
ACCOUNT_SID = "AC7d825129dbb493b9a6847a413997b048"
AUTH_TOKEN = "38274575c6c7a10c4125021498068642"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
    
stock_params = {
    "function" : "TIME_SERIES_DAILY",
    "symbol" : STOCK,
    "apikey" : STOCK_API_KEY
}

url = "https://www.alphavantage.co/query?"
r = requests.get(url, params=stock_params)
r.raise_for_status()
data = r.json()

yesterday_price = float(data['Time Series (Daily)'][str(yesterday)]["4. close"])
before_yesterday_price = float(data['Time Series (Daily)'][str(before_yesterday)]["4. close"])
percentage = (before_yesterday_price - yesterday_price) / before_yesterday_price * 100

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

def finding_article(company):
    global now
    url = "https://newsapi.org/v2/everything?"
    news_params = {
        "q" : company,
        "from" : now,
        "apikey" : NEWS_API_KEY
    }
    r = requests.get(url, news_params)
    r.raise_for_status()
    data = r.json()
    data = data["articles"][:3]
    
    for datum in data:
        print("title : {}".format(datum["title"]))
        print("description : {}".format(datum["description"]))
        print("-" * 100)

if percentage > 5 or percentage < -5:
    print("Start to check the articles for Tesla!")
else:
    finding_article(COMPANY_NAME)

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 
client = Client(ACCOUNT_SID, AUTH_TOKEN)
message = client.messages.create(
    from_="+19805528755",
    to="+447413435831",
    body = "Hi! Are you there kyungyun?",
)

print(message.sid)
#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

