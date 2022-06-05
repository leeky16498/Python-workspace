import datetime as dt
import smtplib
import random
from mail_machine import Sendemail

##___________get current day of the week----------
now = dt.datetime.now()
weekday = now.weekday()

if weekday == 1:
    with open("/Users/kyungyunlee/Desktop/PYTHON/PYTHON_UDEMY/BOOTCAMP_ANGELA/SOURCE_CODES/SMTP_AND_DATE/BIRTHDAY_WISHER/quotes.txt", "r") as file:
        data = file.readlines()
        print(data)
    
    mail_machine = Sendemail(contents=random.choice(data))

##============open the file and make list====

