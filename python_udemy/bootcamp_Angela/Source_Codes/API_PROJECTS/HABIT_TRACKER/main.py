## HTTP requests : get, post, put, delete
import requests 

url = "https://pixe.la/v1/users"

user_params = {
    "token" : "",
    "username" : "Kyungyun Lee",
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes"
}

r = requests.post(url=url, json=user_params)
r.raise_for_status
data = r.json()
print(data)
