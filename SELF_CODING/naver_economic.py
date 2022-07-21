import requests
import smtplib
from email.mime.text import MIMEText
from datetime import datetime

now = datetime.now().strftime("%m/%d/%y")

#-------- 네이버 뉴스 관련 코드 -------#
CLIENT_ID = "geleXkjPByfkP9liYJUB"
CLIENT_SECRET = "Zow_vh_uXo"
API_ENDPOINT = "https://openapi.naver.com/v1/search/news.json"
MY_EMAIL = "leeky16498@gmail.com"
MY_PASSWORD = "tfcawoypiogozmwh"
MAIL_SUBJECT = "하루 시작하며 봐야할 경제 및 기업뉴스 20개 (from. 남편, {})".format(now)
ECO_SUBJECT = "Today's world economy news (from. 남편, {})".format(now)

API_PARAMS = {
    'query' : '산업 미래 투자',
    'display' : 100,
    'start' : 1000,
    'sort' : "sim"
}

API_headers = {
    'X-Naver-Client-Id' : CLIENT_ID,
    'X-Naver-Client-Secret' : CLIENT_SECRET
}

r = requests.get(url=API_ENDPOINT, params=API_PARAMS, headers=API_headers)
r.raise_for_status()
data = r.json()
count = 1
str = "오늘의 <산업, 미래, 투자> 관련 20개 한국 경제뉴스\n\n"

for value in data["items"]:
    if "sid=101" in value["link"]:    
        str += '{}. title : {}\nlink : {}\ndescription: {}\n\n'.format(count, value["title"], value["link"], value["description"])
        count += 1

print(str)

#------영어 경제뉴스 관련 코드 -------#

END_POINT_ECO = 'https://api.apilayer.com/financelayer/news'
API_KEY_ECO = 'nuY2dCxY23Jew5N94vc9EGSS5zVaPEYU'

API_PARAMS_ECO = {
    'date' : 'today',
    'limit' : 15
}

API_HEADERS_ECO = {
    'apikey' : API_KEY_ECO
}

r = requests.get(url=END_POINT_ECO, params=API_PARAMS_ECO, headers=API_HEADERS_ECO)
r.raise_for_status()
eco_data = r.json()
# print(eco_data['data'])
str_eco = "Today's economic news in the world, " + now + "\n\n"
count = 1

for value in eco_data['data']:
    str_eco += '{}. title : {}\nlink : {}\ndescription: {}\n\n'.format(count, value["title"], value["url"], value["description"])
    count += 1

print(str_eco)

#-----email sending----#

smtp = smtplib.SMTP('smtp.gmail.com', 587)
smtp.ehlo()
smtp.starttls()
smtp.login(MY_EMAIL, MY_PASSWORD)

msg = MIMEText(str)
msg['Subject'] = MAIL_SUBJECT

smtp.sendmail(MY_EMAIL, ["leeky16498@gmail.com", "suhyeon106@gmail.com"], msg.as_string())
smtp.close()

#-----email sending----#

smtp = smtplib.SMTP('smtp.gmail.com', 587)
smtp.ehlo()
smtp.starttls()
smtp.login(MY_EMAIL, MY_PASSWORD)

msg = MIMEText(str_eco)
msg['Subject'] = ECO_SUBJECT

smtp.sendmail(MY_EMAIL, ["leeky16498@gmail.com", "suhyeon106@gmail.com"], msg.as_string())
smtp.close()