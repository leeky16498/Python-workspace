with open("python_udemy/bootcamp_Angela/Source_Codes/CSV_processing/weather_data.csv") as data_file:
    data = data_file.readlines()
    print(data)
    
import csv

with open("python_udemy/bootcamp_Angela/Source_Codes/CSV_processing/weather_data.csv") as data_file:
    data = csv.reader(data_file)
    print(data)
    
    temperature = []
    
    for row in data:
        print(row)
        
        if row[1] == "temp":
            continue
        temperature.append(int(row[1]))
    
    
    # 위처럼 데이터 타입을 자유롭게 정렬이 가능해진다.
    # 내부의 데이터를 각 행별로 리스트로 리턴해준다.
    # csv를 통해서 데이터 프로세싱 가능하다.
    print(temperature)
    
