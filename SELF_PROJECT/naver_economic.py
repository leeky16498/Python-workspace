
import requests
import smtplib
from email.mime.text import MIMEText
from datetime import datetime

now = datetime.now().strftime("%m/%d/%y")
CLIENT_ID = "geleXkjPByfkP9liYJUB"
CLIENT_SECRET = "Zow_vh_uXo"
API_ENDPOINT = "https://openapi.naver.com/v1/search/news.json"
MY_EMAIL = "leeky16498@gmail.com"
MY_PASSWORD = "tfcawoypiogozmwh"
MAIL_SUBJECT = "하루 시작하며 봐야할 경제 및 기업뉴스 20개 (from. 남편, {}])".format(now)

API_PARAMS = {
    'query' : '경제 기업',
    'display' : 20,
    'start' : 1,
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
str = "오늘의 경제 및 기업관련 20개 네이버 뉴스\n\n"

for value in data["items"]:
    str += '{}. title : {}\nlink : {}\n\n'.format(count, value["title"], value["link"])
    count += 1

print(str)

#-----email sending----#

smtp = smtplib.SMTP('smtp.gmail.com', 587)
smtp.ehlo()
smtp.starttls()
smtp.login(MY_EMAIL, MY_PASSWORD)

msg = MIMEText(str)
msg['Subject'] = MAIL_SUBJECT

smtp.sendmail(MY_EMAIL, ["leeky16498@gmail.com", "suhyeon106@gmail.com"], msg.as_string())
smtp.close()
