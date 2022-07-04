import requests
import gspread

EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
APP_ID = "5896ec12"
APP_KEY = "7c16c840a288db0652381cd5d26991be"

headers = {
    "x-app-id" : APP_ID,
    "x-app-key" : APP_KEY,
}

request_body = {
    "query":"ran 3 miles",
    "gender":"male",
    "weight_kg":106.5,
    "height_cm":183.4,
    "age":30
}

r = requests.post(url=EXERCISE_ENDPOINT, json=request_body, headers=headers)
r.raise_for_status()
data = r.json()
print(data)

sa = gspread.service_account("/Users/kyungyunlee/Desktop/PYTHON/PYTHON_UDEMY/BOOTCAMP_ANGELA/SOURCE_CODES/API_PROJECTS/WORKOUT_TRACKING/argon-depot-355312-a49813daaac7.json")
sh = sa.open("googlesheettest")

wks = sh.worksheet("test data")
#------getting data-----
print("rows :", wks.row_count)
print("cols :", wks.col_count)

print(wks.acell('A9').value)
print(wks.cell(3, 4).value)
print(wks.get('A7:E9'))
print(wks.get_all_records())

wks.append_row(["Lee", 17, 38])
# wks.update('A3', 'Lee')
# wks.update('D2:E3', [["Engineering, Tennis"], ["Business", "Poetry"]])
# wks.update('F2', '=UPPER(E2)', raw=False)

# wks.delete_rows(25)