### 파일 프린트 저장 개념 ###

score_file = open("score.txt", "w", encoding="utf8")
# 오픈할 파일명, 그리고 읽기 전용, 인코딩의 형태를 정의한다.
print("수학 : 0", file = score_file)
print("영어 : 50", file = score_file)
score_file.close()
#파일이 없으면 생성이 되고 그 안에 내용이 들어가게 된다.
# "w" : writing, "r" = reading, "wb" = 바이너리 값으로 저장하라는 의미이다.

# score_file = open("score.txt", "a", encoding="utf8")
# #덮어쓰기 할때는 "a"를 입력해서 나타내준다.
# score_file.write("\n과학 : 80")
# score_file.write("\n코딩 : 100")
# score_file.close()

#스코어 파일을 열어서 해당 내용들을 읽어 올 수 있다 "r"키워드
# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.read())
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.readline(), end = "")
# print(score_file.readline())
# print(score_file.readline())
# print(score_file.readline())
# score_file.close()
# #줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동

# score_file = open("score.txt", "r", encoding="utf8")
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line, end="")
#     #end를 변경해주면 줄바꿈이 사라지게 된다.
# score_file.close()

score_files = open("score.txt", "r", encoding="utf8")
lines = score_files.readlines() #리스트 형태로 저장해준다.
for line in lines:
    print(line, end="")

score_files.close()
