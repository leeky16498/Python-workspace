from turtle import Turtle

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.high_score = self.open_data_file()
        self.penup()
        self.goto(0, 170)
        self.write(f"Score : {self.score}", align="center", font=("Arial", 24, "normal"))
        self.hideturtle()
        print(self.high_score)
        
    def open_data_file(self):
        with open("/Users/kyungyunlee/Desktop/Python_udemy/PythonUdemy/Source_Codes/Snake_Game/data.txt", "r") as file:
            data = file.read()
            print(data)
            self.high_score = int(data)
        
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score : {self.score}", align="center", font=("Arial", 24, "normal"))
    
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
    
    def game_over(self):
        self.goto(0,0)
        self.write("Game_Over", align="center", font=("Arial", 24, "normal"))
    
    def reset(self):
        
        if self.score > self.high_score:
            self.high_score = self.score
            
            with open("/Users/kyungyunlee/Desktop/Python_udemy/PythonUdemy/Source_Codes/Snake_Game/data.txt", "w") as file:
                data.write(self.high_score)
            
        self.score = 0
        self.update_scoreboard()