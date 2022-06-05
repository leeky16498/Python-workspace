import requests
from datetime import datetime
from mail_machine import Sendemail
import threading
import time

MY_LAT = 51.507351 # Your latitude
MY_LONG = -0.127758 # Your longitude

def check_iss_location():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the ISS position.    

    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    print(sunset)
    print(time_now.hour)

    #If the ISS is close to my current position
    # and it is currently dark 지금은 어둡다 따라서 선셋을 가져오고
    # Then send me an email to tell me to look up. 위를 보 라고 메일을 보내준다.
    # BONUS: run the code every 60 seconds.

    if iss_latitude-5 <= MY_LAT <= iss_latitude+5 and iss_longitude-5 <= MY_LONG <= iss_longitude+5 and time_now.hour > sunset:
        sender = Sendemail("ISS is on your head!", "Hi!, on your head, the ISS is there! Look at the sky now!")
        
    threading.Timer(60, check_iss_location).start()
    ## 스레딩을 통해서 원하는 함수의 반복 수행을 제어해 줄 수 있다.

check_iss_location()