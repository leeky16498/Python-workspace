import requests
from twilio.rest import Client

OWM_ENDPOINT = "https://api.openweathermap.org/data/3.0/onecall"
API_KEY = "fa0cff1c4cd7c8a9dd28bbef2155cfff"

## twilio
ACCOUNT_SID = "AC7d825129dbb493b9a6847a413997b048"
AUTH_TOKEN = "38274575c6c7a10c4125021498068642"

weather_params = {
    "lat" : 51.507351,
    "lon" : -0.127758,
    "appid" : API_KEY, # 마지막에도 쉼표 찍어줘야 한다.
    "exclude" : "current,minutely,daily",
}

response = requests.get(OWM_ENDPOINT, params=weather_params)
weather_data = response.json()
print(weather_data)

# weather_slice = weather_data["hourly"][:12] # 리스트 슬라이싱을 시도한다.
will_rain = False

# for hour_data in weather_slice:
#     condition_code = hour_data["weather"][0]["id"]
#     if int(condition_code) < 700:
#         will_rain = True
        
if will_rain:
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages.create(  
                              messaging_service_sid='AC7d825129dbb493b9a6847a413997b048', 
                              body='hi there Lee!',      
                              to='+447413435831' 
                          ) 
    print(message.status)
    
