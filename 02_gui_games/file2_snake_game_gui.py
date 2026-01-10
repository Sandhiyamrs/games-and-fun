import turtle
import time

screen = turtle.Screen()
screen.title("Snake Game")
screen.bgcolor("black")

snake = turtle.Turtle()
snake.shape("square")
snake.color("green")
snake.penup()

def move():
    snake.forward(20)
    screen.ontimer(move, 100)

move()
screen.mainloop()
