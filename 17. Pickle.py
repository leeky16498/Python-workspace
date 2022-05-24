### pickle 개념 정리 ###

import pickle
from profile import Profile

profile_file = open("profile.pickle", "wb")
# 피클로 저장할때는 반드시 쓰기 타입을 바이너리로 설정해주어야 한다.
# 피클에서는 읽기와 바이너리 타입을 반드시 설정해줘야 하며, 인코딩에 대해서는 설정할 필요없다.

profile = {"이름" : "박명수", "나이" : 30, "취미" : ["축구", "골프", "코딩"]}
# 데이터 타입에 구애받지 않고 다양한 데이터를 넣을 수 있다.

print(Profile)
pickle.dump(profile, profile_file)
# profile에 있는 정보를 profile_file에 저장한다.
profile_file.close()
# 파일을 닫아준다.
# 데이터를 피클을 통해서 저장하고 이를 불러다가 쓸 수 있는 라이브러리이다.

profile_file1 = open("profile.pickle", "rb")
# 읽기 전용으로 사용해도 b를 붙여서 바이너리 타입으로 사용함을 명시해준다.

profile1 = pickle.load(profile_file1)
#파일을 열어서 데이터를 가져온다.

print(profile1)

# with에 대해서 알아본다.

import pickle

with open("profile.pickle", "rb") as profile_file2:
    print(pickle.load(profile_file2))
# 위에서 사용한 것이랑 같은 결과를 나타내주는데 별도로 파일을 열고 닫을 필요가 없다.
# with를 사용하게 되면 하나의 클로저 속에서 바로바로 파일 읽기 쓰기를 수행할 수 있다.

# 피클 사용없이 일반적으로 파일을 열고 닫으면서 파일정보를 가져와본다.
with open("study.txt", "w", encoding="utf8") as study_file:
    study_file.write("파이썬 죽어라 공부중입니다.")

with open("study.txt", "r", encoding="utf8") as study_file1:
    print(study_file1.read())

# 피클사용없이 파일을 열고 그 정보를 가져왔다. with 모듈을 사용해서 처리가 가능하다.

# for i in range(1, 51):
#     with open(str(i) + "주차.txt", "w", encoding="utf8") as report_file:
#         report_file.write("- {0} 주차 주간보고 -".format(i))
#         report_file.write("\n부서 : ")
#         report_file.write("\n이름 : ")
#         report_file.write("\n업무요약 : ")
        # /n을 사용하면 줄바꿈을 해준다.