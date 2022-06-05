import datetime as dt
import pandas as pd
import random
from mail_machine import Sendemail


now = dt.datetime.now()
today_tuple = (now.month, now.day)

data = pd.read_csv("/Users/kyungyunlee/Desktop/PYTHON/PYTHON_UDEMY/BOOTCAMP_ANGELA/SOURCE_CODES/SMTP_AND_DATE/BIRTH_MESSAGE_EXTRAHARD/birthdays.csv")

bir_dict = {
    (data_row["month"], data_row["day"]) : data_row for (index, data_row) in data.iterrows()
}

print(bir_dict)
# 이게 모노스페이스 였구나 ㅋㅋㅋ신기하네 ㅋㅋㅋ

if today_tuple in bir_dict:
    bir_person = bir_dict[today_tuple]
    file_path = f"/Users/kyungyunlee/Desktop/PYTHON/PYTHON_UDEMY/BOOTCAMP_ANGELA/SOURCE_CODES/SMTP_AND_DATE/birthday-wisher-extrahard-start/letter_templates/letter_{random.randint(1,3)}.txt"
    
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]",bir_person.name)
    
    sender = Sendemail(contents=contents)