import requests
import datetime as dt

my_lat = 51.507351
my_lng = -0.12775
my_formatted = 0

parameters = {
    "lat" : my_lat,
    "lng" : my_lng
}

response = requests.get(url="https://api.sunrise-sunset.org/json?formatted=0", params=parameters)
# 뒤에?붙여준다음에 파라미터를 자유롭게 조절해줄 수 있다.
response.raise_for_status()

data = response.json()
print(data)

##돌아온 데이터에서 키 값을 통해서 밸류를 꺼내준다.

sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

time_now = dt.datetime.now()
print(time_now)
print(sunrise)
print(sunset)