import tkinter as tk
import random
import time

root = tk.Tk()
root.title("🃏 Memory Match Game")

buttons = []
values = list(range(1, 9)) * 2
random.shuffle(values)

first = None
second = None
matched = 0

def check_match():
    global first, second, matched

    if values[first] == values[second]:
        buttons[first].config(text=values[first], state="disabled")
        buttons[second].config(text=values[second], state="disabled")
        matched += 1
    else:
        buttons[first].config(text="")
        buttons[second].config(text="")

    first = None
    second = None

def click(i):
    global first, second

    if first is None:
        first = i
        buttons[i].config(text=values[i])
    elif second is None and i != first:
        second = i
        buttons[i].config(text=values[i])
        root.after(700, check_match)

for i in range(16):
    btn = tk.Button(root, text="", width=5, height=2, command=lambda i=i: click(i))
    btn.grid(row=i//4, column=i%4)
    buttons.append(btn)

root.mainloop()
