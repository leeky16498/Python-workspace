import requests
import pywhatkit as pwk

CLIENT_ID = "geleXkjPByfkP9liYJUB"
CLIENT_SECRET = "Zow_vh_uXo"
API_ENDPOINT = "https://openapi.naver.com/v1/search/news.json"

API_PARAMS = {
    'query' : '경제 top',
    'display' : 10,
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
print(data["items"])
count = 1
str = ""


for value in data["items"]:
    str += '{}. title : {}\nlink : {}\n\n'.format(count, value["title"], value["link"])
    count += 1
    
pwk.sendwhatmsg("+447413435831", str, 7, 26)