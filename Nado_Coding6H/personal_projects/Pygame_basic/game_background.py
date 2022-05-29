## 파이썬 활용 첫번쨰 : 풍선 부시기 팡팡게임

import pygame

#파이게임의 뼈대를 만든다.
pygame.init() #모듈 초기화

#화면 크기 설정
screen_width = 480 # 가로
screen_height = 640 # 세로
screen = pygame.display.set_mode((screen_height, screen_height)) # 스크린 생성

##화면 타이틀 설정
pygame.display.set_caption("Kyungyun's game")

## 배경이미지 불러오기
# background = pygame.image.load("/Users/kyungyunlee/Desktop/PYTHON DOCUMENTS/Nado_Coding6H/personal_projects/Pygame_basic/Background.png")
# 파일 우클릭 후, 경로 복사하면 된다. 이미지를 불러온 상태인데 아직 그린건 아니다.

#이벤트 루프
is_game_running = True # 게임 진행중 여부 확인

while is_game_running:
    for event in pygame.event.get(): # 어떤 이벤트가 게임에서 발생하는가?
        if event.type == pygame.QUIT:
            is_game_running = False # 만약 윈도우 클로즈 버튼을 누르면 게임을 종료한다.

    screen.fill((0, 0, 255))
    # screen.blit(background, (0,0)) # 배경 그리기, 매개변수로 백그라운드를 넣어준다.
    pygame.display.update()

# 게임이 켜지면, 이벤트 루프가 계속해서 돌고있는 상태이므로, 창이 꺼지지 않는다.



# 게임 종료시 파이게임 종료
pygame.quit()