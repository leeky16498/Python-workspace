from email import message
import requests
import gspread
from twilio.rest import Client

#0. constants ---------------
KIWI_API_KEY = "ZG_Y95H5byN-t9BYotdNNL8NL7dazbtz"
ACCOUNT_SID = "AC7d825129dbb493b9a6847a413997b048"
AUTH_TOKEN = "38274575c6c7a10c4125021498068642"
KIWI_ENDPOINTS = "https://tequila-api.kiwi.com/locations/query"

# 1. spreadsheet using condition set up
sa = gspread.service_account("/Users/kyungyunlee/Desktop/PYTHON/PYTHON_UDEMY/BOOTCAMP_ANGELA/SOURCE_CODES/API_PROJECTS/WORKOUT_TRACKING/argon-depot-355312-a49813daaac7.json")
sh = sa.open("Flight Deals")
wks = sh.worksheet("prices")
all_places = wks.get_all_records()


#2. searching air tickets with tequila

def search_citycode(city_name):
    headers = {
        "apikey" : KIWI_API_KEY
    }

    kiwi_params = {
        "term" : city_name,
        "location_types" : "city"
    }

    r = requests.get(url=KIWI_ENDPOINTS, params=kiwi_params, headers=headers)
    r.raise_for_status()
    data = r.json()
    return data["locations"][0]["code"]

for i in range(len(all_places)):
    wks.update('B{}'.format(i+2), search_citycode(all_places[i]["City"]))
    

# 2. twilio environment setting 
# client = Client(ACCOUNT_SID, AUTH_TOKEN)
# message = client.messages.create(
#     from_="+19805528755",
#     to="+447413435831",
#     body="The message I want to send"
# )