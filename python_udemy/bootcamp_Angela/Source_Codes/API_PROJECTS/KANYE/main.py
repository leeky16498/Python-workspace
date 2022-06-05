## API : Aplication programming Interface 사용자와 웹사이트의 상호작용을 중재하는 것. 인터페이스이다. 일종의 장벽이고.
## API가 규정한 틀에 따라서 외부 시스템에 자료를 요청하게 된다.

### iss location API를 사용해서 요청을 보내보자
import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
# print(response.status_code)

# if response.status_code == 404:
#     raise Exception("That resource is not correct")
## 커스텀 에러처리가 가능하다.

response.raise_for_status()

data = response.json()##넘어온 JSON파일을 처리하는 메서드

iss_longitute = data["iss_position"]["longitude"]
iss_latitude = data["iss_position"]["latitude"]

iss_position = (iss_latitude, iss_longitute)
print(iss_position)
##딕셔너리를 통해서 직접적으로 데이터 접근이 가능하다.
print(data)



##1xx : Hold on(진행중)
##2xx : Here you go(성공)
##3xx : Go Away
##4xx : You screwed up
##5xx : I screwed up