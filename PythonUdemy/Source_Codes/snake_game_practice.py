from turtle import Screen, Turtle, bgcolor
import turtle

screen = Screen()
screen.setup(600, 400)
screen.bgcolor("black")
screen.title("Snake Game")

turtles = []

for index in range(3):
    new_turtles = Turtle("square")
    new_turtles.penup()
    new_turtles.color("white")
    new_turtles.setpos(20*index, 0)
    turtles.append(new_turtles)

screen.exitonclick()