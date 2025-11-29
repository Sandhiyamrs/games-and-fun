# Snake Game GUI using Tkinter
import tkinter as tk
import random

root = tk.Tk()
root.title("Snake Game")

canvas = tk.Canvas(root, width=400, height=400, bg="black")
canvas.pack()

snake = [(20,20)]
food = (100,100)
direction = "Right"
size = 20

def draw():
    canvas.delete("all")
    for x,y in snake:
        canvas.create_rectangle(x, y, x+size, y+size, fill="green")
    fx, fy = food
    canvas.create_rectangle(fx, fy, fx+size, fy+size, fill="red")

def move():
    global snake, food
    x, y = snake[-1]
    if direction=="Right":
        x += size
    elif direction=="Left":
        x -= size
    elif direction=="Up":
        y -= size
    elif direction=="Down":
        y += size
    snake.append((x,y))
    if (x,y) == food:
        food = (random.randint(0,19)*size, random.randint(0,19)*size)
    else:
        snake.pop(0)
    draw()
    root.after(200, move)

def key(event):
    global direction
    if event.keysym in ["Left","Right","Up","Down"]:
        direction = event.keysym

root.bind("<Key>", key)
move()
root.mainloop()

