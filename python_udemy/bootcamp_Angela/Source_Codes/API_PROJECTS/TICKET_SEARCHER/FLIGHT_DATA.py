import requests 
from datetime import datetime, timedelta

now = datetime.now()
now = now.date()
date_from = now.strftime("%d/%m/%Y")
date_to = (now+timedelta(days=180)).strftime("%d/%m/%Y")
print(date_to)

class FlightData:
    def __init__(self):
        global date_to
        self.fly_from = "LON"
        self.date_to = date_to

    def search_filght(self, fly_to):
        global date_from, date_to
        ticket_endpoint = "https://tequila-api.kiwi.com/v2/search"

        ticket_params = {
            "fly_from" : "LON",
            "fly_to" : fly_to,
            "date_from" : date_from,
            "date_to" : date_to,
            "nights_in_dst_from" : 7,
            "nights_in_dst_to" : 28,
            "flight_type" : "round"
        }

        headers = {
            "apikey" : "ZG_Y95H5byN-t9BYotdNNL8NL7dazbtz"
        }
        
        r = requests.get(url=ticket_endpoint, params=ticket_params, headers=headers)
        r.raise_for_status()
        data = r.json()
      
        return data["data"][0]["price"]