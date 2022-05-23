# 외장함수는 내장과 다르게 임폴트를 해서 사용해야하는 것들이다.

# glob : 경로내의 파일 및 폴더 목록을 조회하는 것이다.
import glob
print(glob.glob("*.py"))
# 확장자가 .py인 모든 친구들의 리스트를 불러준다.

# os : 운영체제에서 제공하는 기본 기능이다.

import os
print(os.getcwd())
#현재 파일이 위치한 디렉토리를 표현해준다.

folder = "sample_dir"

if os.path.exists(folder):
    print("이름이 존재하는 폴더입네다.")
    os.rmdir(folder)
    print("폴더를 삭제헀습니다.")
else:
    os.makedirs(folder)
    print(folder, "폴더를 생성했습니다.")

print(os.listdir())
#이렇게 하면 폴더안에 있는 모든 파일리스트를 띄워준다.

import time 
# 시간관련 함수를 제공해준다.

print(time.localtime())
print(time.strftime("%Y-%m-%d %H:%M:%S"))

import datetime
print(datetime.date.today())
#timedelta : 두 날짜간의 간격을 알려준다.

today = datetime.date.today()
td = datetime.timedelta(days=100)
print("우리 만난지 100일은?{0}".format(today + td))