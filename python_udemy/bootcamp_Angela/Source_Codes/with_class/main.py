file = open("/Users/kyungyunlee/Desktop/Python_udemy/PythonUdemy/Source_Codes/with_class/my_file.txt")
#open 메서드를 통해서 파일 열기가 가능하다. 
#read 메서드를 통해서 파일 읽기가 가능하다.
contents = file.read()
print(contents)
file.close()
# 굳이 닫아주는 이유는 메모리를 좀 아끼자랄까?
# 파일을 닫아주는 메서드를 실행 가능하다.

with open("/Users/kyungyunlee/Desktop/Python_udemy/PythonUdemy/Source_Codes/with_class/my_file.txt") as file:
    contents = file.read()
    print(contents)

# 다음과 같이 with를 해주면, 별도로 파일을 열고닫는 것을 신경쓰지 않아도 된다.
# 위의 코드들과 동일하게 작동한다.

#이번에는 써보자.
with open("my_file.txt", mode="w") as file:
    file.write("New text is here!!!!!!!!!!!!!!")
# 읽기 전용에서는 "r" 모드로 써준다.
# 텍스트가 위의 텍스트로 전부 바뀐다.
# 모드를 "a"를 쓰면 추가된다.

with open("/Users/kyungyunlee/Desktop/Python_udemy/PythonUdemy/Source_Codes/with_class/my_file.txt", mode="a") as file:
    file.write("New text is here! with append function!")

# 파일이 존재하지 않을 수 있으므로, 파일을 새로 만들면서 시작해보자.

with open("/Users/kyungyunlee/Desktop/Python_udemy/PythonUdemy/Source_Codes/with_class/my_file_more.txt", mode="w") as file:
    file.write("New text is here! with you.")
    
# 읽기 모드로 없는 파일명에 접근하면 새파일을 생성한다.