from turtle import Turtle, Screen
from word_turtle import Word
import pandas as pd
import time

screen = Screen()
screen.title("USA Quiz")
screen.bgpic("/Users/kyungyunlee/Desktop/PYTHON/python_udemy/bootcamp_Angela/Source_Codes/PANDAS_boot/us-states-game-start/blank_states_img.gif")

data = pd.read_csv("/Users/kyungyunlee/Desktop/PYTHON/python_udemy/bootcamp_Angela/Source_Codes/PANDAS_boot/us-states-game-start/50_states.csv")
print(data)

usa_area = data.state.to_list()
usa_x = data.x.to_list()
usa_y = data.y.to_list()
print(usa_area)
print(usa_x)
print(usa_y)

usa_dict = {}

for i in range(len(usa_area)):
    usa_dict[usa_area[i]] = (usa_x[i], usa_y[i])

print(usa_dict)

is_game_on = True

saved_area = {
    "answered_area" : [],
    "coordinates_x" : [],
    "coordinates_y" : []
}

while is_game_on:
    
    answer_state = screen.textinput(title="Guess the state", prompt="What is another states name?")

    if answer_state in usa_area:
        coor = usa_dict[answer_state]
        print(coor)
        word = Word()
        word.goto(coor[0], coor[1])
        
        saved_area["answered_area"].append(answer_state)
        saved_area["coordinates_x"].append(coor[0])
        saved_area["coordinates_y"].append(coor[1])
        print(saved_area)
        
        
    else:
        print("Game is over")
        df = pd.DataFrame(saved_area)
        df.to_csv("/Users/kyungyunlee/Desktop/PYTHON/python_udemy/bootcamp_Angela/Source_Codes/PANDAS_boot/us-states-game-start/50_states_answered.csv")
    
    time.sleep(0.5)

screen.mainloop()
# 이렇게 해주면 계속해서 창이 떠있게 된다.
