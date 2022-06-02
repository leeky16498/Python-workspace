import pandas

##데이터 분석을 용이하게 해주기 위한 유명한 라이브러리이다.

data = pandas.read_csv("python_udemy/bootcamp_Angela/Source_Codes/CSV_processing/weather_data.csv")
# print(data)
# print(data["temp"])

# # 판다스는 마지막에 데이터 타입을 같이 출력해준다.

# data_dict = data.to_dict()
# print(data_dict)
# #데이터를 딕셔너리로 변경해준다.

# temp_list = data["temp"].to_list()
# print(temp_list)
# # 데이터를 리스트로 나열해준다.

# print(data["temp"].mean())
# print(data["temp"].max())
# print(data["temp"].min())
# print(data.temp)
# # 이렇게 데이터이름을 객체처럼 취급해서 접근이 가능하다.
# print(data.condition)
# # 이렇게 데이터이름을 객체처럼 취급해서 접근이 가능하다.


## 행 데이터를 가져오는 법
print(data[data.day == "Monday"])

#가장 높은 온도의 행을 출력하는 법
print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
monday_temp = monday.temp
print(monday_temp)

data_dict = {
    "student" : ["Amy", "James", "Angela"],
    "scores" : [76, 56, 65]
}

# 위의 딕셔너리를 csv프레임으로 만든다.

data1 = pandas.DataFrame(data_dict)
print(data1)
data1.to_csv("python_udemy/bootcamp_Angela/Source_Codes/CSV_processing/new_data.csv")