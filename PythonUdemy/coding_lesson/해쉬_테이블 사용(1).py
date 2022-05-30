
students = ["Mike", "Steve", "Mike", "Ana", "Mike"]
# students_passing = ["Kim", "Lee"]
students_passing = ["Mike", "Steve", "Ana"]
## will return "Park"
## 동명이인을 고려한다.

# students = ["Kim", "Lee", "Park", "Me"]

def find_students(students):
    
    students_dic = {}
    
    for student in students:
        if student in students_passing:
            students_dic[student] = students.count(student)
        else:
            students_dic[student] = 0

    print(students_dic)

    for key, value in students_dic.items():
        if value == 0:
            return key
        
        elif value >= 2:
            return (key + ", ") * (value-1)

sol1 = find_students(students)
print(sol1)
