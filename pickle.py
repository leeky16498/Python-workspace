#pickle에 대해서 알아본다.

import pickle
from profile import Profile

profile_file = open("profile.pickle", "wb")
# 피클에서는 읽기와 바이너리 타입을 반드시 설정해줘야 하며, 인코딩에 대해서는 설정할 필요없다.

profile = {"이름" : "박명수", "나이" : 30, "취미" : ["축구", "골프", "코딩"]}

print(Profile)
pickle.dump(profile, profile_file)
# profile에 있는 정보를 file에 저장한다.
profile_file.close()

#데이터를 피클을 통해서 저장하고 이를 불러다가 쓸 수 있는 라이브러리이다.

profile_file1 = open("profile.pickle", "rb")
profile1 = pickle.load(profile_file1)
#파일을 열어서 데이터를 가져온다.
print(profile1)

# with에 대해서 알아본다.

import pickle

with open("profile.pickle", "rb") as profile_file2:
    print(pickle.load(profile_file2))

# 위에서 사용한 것이랑 같은 결과를 나타내주는데 별도로 파일을 열고 닫을 필요가 없다.

# 피클사용없이 일반적으로 파일을 열고 닫으면서 파일정보를 가져와본다.
with open("study.txt", "w", encoding="utf8") as study_file:
    study_file.write("파이썬 죽어라 공부중입니다.")

with open("study.txt", "r", encoding="utf8") as study_file1:
    print(study_file1.read())
    
# 피클사용없이 파일을 열고 그 정보를 가져왔다. with 모듈을 사용해서 처리가 가능하다.