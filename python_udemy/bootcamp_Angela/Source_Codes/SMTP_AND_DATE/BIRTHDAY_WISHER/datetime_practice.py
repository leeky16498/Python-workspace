import datetime as dt

now = dt.datetime.now()
print(now)

year = now.year
month = now.month

print(year, month)

day_of_week = now.weekday()
print(day_of_week)
## 일요일이라서 인덱스 6을 찍어낸다.

date_of_birth = dt.datetime(year=1988,month=1, day=13)
print(date_of_birth)
# 날짜 데이터를 형식에 맞게 출력해준다.
