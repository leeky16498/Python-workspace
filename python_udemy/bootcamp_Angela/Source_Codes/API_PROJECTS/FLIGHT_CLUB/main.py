import requests
import gspread 

# 0. constants and keys
GOOGLE_CLOUD_KEY = "/Users/kyungyunlee/Desktop/PYTHON/PYTHON_UDEMY/BOOTCAMP_ANGELA/SOURCE_CODES/API_PROJECTS/WORKOUT_TRACKING/argon-depot-355312-a49813daaac7.json"
KIWI_API_KEY = "ZG_Y95H5byN-t9BYotdNNL8NL7dazbtz"
ACCOUNT_SID = "AC7d825129dbb493b9a6847a413997b048"
AUTH_TOKEN = "38274575c6c7a10c4125021498068642"
KIWI_ENDPOINTS = "https://tequila-api.kiwi.com/locations/query"

# 1. making spreadsheet for getting user information

sa = gspread.service_account(GOOGLE_CLOUD_KEY)
sh = sa.open("Flight Deals")
wks = sh.worksheet("Users")

#2. get information from input + email confirmation

user_surname = input("what is your surname?  ")
user_firstname = input("What is your first name?  ")
user_email = input("What is your email?  ")
user_email_confirm = input("Confirm your email (one more!)  ")
ALL_INFORMATION_GOOD = True

if user_email == user_email_confirm:
    wks.append_row([user_surname, user_firstname, user_email])
else:
    ALL_INFORMATION_GOOD = False

while not ALL_INFORMATION_GOOD:
    print("Check your email one more please")
    user_email = input("What is your email?  ")
    user_email_confirm = input("Confirm your email (one more!)  ")
    
    if user_email == user_email_confirm:
        wks.append_row([user_surname, user_firstname, user_email])
        ALL_INFORMATION_GOOD = True
        
#3. Looking for the lowest Price of Ticket in 6 month

def search_lowest_ticket():
    headers = {
        "apikey" : KIWI_API_KEY
    }
    
    kiwi_params = {
        "term"
    }