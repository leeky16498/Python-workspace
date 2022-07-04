## HTTP requests : get, post, put, delete
import requests 
from datetime import datetime

url = "https://pixe.la/v1/users"

USERNAME = "devleeky16498"
TOKEN = "dlruddbs2@"

PIXELA_ENDPOINT = "https://pixe.la/v1/users"

user_params = {
    "token" : TOKEN,
    "username" : USERNAME,
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes"
}

# r = requests.post(url=url, json=user_params)
# r.raise_for_status
# data = r.json()
# print(data)

GRAPH_ID = "graph1"
graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"

graph_config = {
    "id" : GRAPH_ID,
    "name" : "Cycling Graph",
    "unit" : "Km",
    "type" : "float",
    "color" : "ajisai"
}

headers = {
    "X-USER-TOKEN" : TOKEN
}

r = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
r.raise_for_status()
data = r.json()
print(data)

post_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"
today = datetime.now()

post_config = {
    "date" : today.strftime("%Y%m%d"),
    "quantity" : "5",
}

post_headers = {
    "X-USER-TOKEN" : TOKEN
}

# r = requests.post(url=post_endpoint, json=post_config, headers=post_headers)
# r.raise_for_status()
# data = r.json()
# print(data)

update_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime("%Y%m%d")}"

new_pixel_data = {
    "quantity" : "4.5"
}

requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
requests.delete(url=update_endpoint, headers=post_headers)