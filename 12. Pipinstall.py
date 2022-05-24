# 파이선에는 정말 다양한 라이브러리가 존재한다 pypi에 가면 진짜 수도없이 많다.
# 인스톨 할때는 pip3 install [library name]
# 언인스톨 때는 pip3 uninstall[library name]

# 사용할때 예시(인스톨 후)

from bs4 import BeautifulSoup
soup = BeautifulSoup()
print(soup.pretty())

# 다음은 뷰티풀수프라는 웹 크롤링 라이브러리를 사용하는 예시이다.
# 외장함수를 임폴트 한후, 객체를 생성하고 실제 사용한다.