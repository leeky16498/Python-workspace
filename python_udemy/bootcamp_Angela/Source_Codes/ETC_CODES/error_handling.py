#대표적인 에러들
# FileNotFoundError : 쓰기에서 읽기 전용을 실행할 때,
# KeyError : 딕셔너리에서 키에 해당하는 값이 없을 때,
# IndexError : 리스트 인덱스를 넘어갈 때
# TypeError : 타입이 맞지 않을 때, 

##위의 에러들을 처리하기 위해서 우리는 에러 핸들링을 실시한다.

'''
1. try : something that might cause an exception
2. except : Do this if there was an exception
3. else: Do this if there were no exception
4. finally : Do this no matter what happens

'''

try:
    file = open("a_file.txt")
except:
    file = open("a_file.txt", "w")
    file.write("something")
    
try:
    file = open("a_file.txt")  
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("something")
except KeyError as error:
    print("fcu!" + error)
## 다음과 같이 구체적인 에러의 발생에 대해서도 가지치기가 가능하다.
# as 구문으로 error를 연관값으로 체크해서 전달이 가능하다.
else:
    print("hahah")
    ##여기는try에서 에러체크가 안될 때 씰행된다.
finally:
    file.close()
    ##여기는 무조건 이 마지막에 상관없이 실행된다.
    
    
## 조건문처럼 에러를 핸들링해서 프로그램의 강제 종료를 막는다.