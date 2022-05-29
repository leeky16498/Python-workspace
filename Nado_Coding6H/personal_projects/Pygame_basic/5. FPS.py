## 파이썬 활용 첫번쨰 : 풍선 부시기 팡팡게임

from tkinter import EventType
import pygame

#파이게임의 뼈대를 만든다.
pygame.init() #모듈 초기화

#화면 크기 설정
screen_width = 480 # 가로
screen_height = 640 # 세로
screen = pygame.display.set_mode((screen_height, screen_height)) # 스크린 생성

##화면 타이틀 설정
pygame.display.set_caption("Kyungyun's game")

#FPS객체 생성 후 clock에 넣어줌
clock = pygame.time.Clock()


## 배경이미지 불러오기
# background = pygame.image.load("/Users/kyungyunlee/Desktop/PYTHON DOCUMENTS/Nado_Coding6H/personal_projects/Pygame_basic/Background.png")
# 파일 우클릭 후, 경로 복사하면 된다. 이미지를 불러온 상태인데 아직 그린건 아니다.

# 캐릭터(스프라이트 불러오기)
character = pygame.image.load("/Users/kyungyunlee/Desktop/PYTHON DOCUMENTS/Nado_Coding6H/personal_projects/Pygame_basic/character.png")
character_size = character.get_rect().size # 이미지의 가로세로를 가져온다
character_width = character_size[0] # 캐릭터 가로
character_height = character_size[1] # 캐릭터 세로
character_x_pos = screen_width/2 + character_width # 화면 가로크기의 절반에 위치하도록 설정
character_y_pos = screen_height - character_height # 화면 세로크기의 가장 아래 설정

to_x = 0
to_y = 0
#캐릭터가 이동할 좌표

#캐릭터 이동속도
character_speed = 0.6

#이벤트 루프
is_game_running = True # 게임 진행중 여부 확인

while is_game_running:

    dt = clock.tick(60)# 게임의 프레임 수를 결정한다.,원하는 프레임 수를 인티저로 넣어준다.
    # 프레임이 높아질수록 훨씬 움직임이 부드럽다.
    # 캐릭터가 1초에 100만큼 이동해야 함
    # 10fps : 1초간 10번 동작 -> 1번에 몇만큼 이동? 10만큼, 10*10 = 100
    # 20fps : 1초간 20번 동작 -> 1번에 5만큼 이동해야함, 5 * 20 = 100
    # 프레임별로 이동하는 거리가 달라져야 한다.

    print("fps :" + str(clock.get_fps()))

    for event in pygame.event.get(): # 어떤 이벤트가 게임에서 발생하는가?
        if event.type == pygame.QUIT:
            is_game_running = False # 만약 윈도우 클로즈 버튼을 누르면 게임을 종료한다.
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT: # 왼쪽키를 누르믄 캐릭터가 왼쪽으로 움직이면 된다.
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            elif event.key == pygame.K_UP:
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:
                to_y += character_speed
        #유저가 키에서 손을 때면, 다음과 같이 처리해라, 방향키를 떼면 캐릭터가 멈추도록 처리
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
# 다음 조건문을 통해서 가로 움직임이 스크린을 벗어나지 않도록 처리.

    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    screen.fill((0, 0, 255))
    screen.blit(character, (character_x_pos, character_y_pos))
    # screen.blit(background, (0,0)) # 배경 그리기, 매개변수로 백그라운드를 넣어준다.
    pygame.display.update()

# 게임이 켜지면, 이벤트 루프가 계속해서 돌고있는 상태이므로, 창이 꺼지지 않는다.

# 게임 종료시 파이게임 종료
pygame.quit()