import tkinter as tk
import random

root = tk.Tk()
root.title("Memory Match")

values = list("AABBCCDDEEFF")
random.shuffle(values)

buttons = []
first = None

def click(btn, value):
    global first
    btn.config(text=value)
    if not first:
        first = (btn, value)
    else:
        if first[1] != value:
            root.after(500, lambda: hide(btn, first[0]))
        first = None

def hide(b1, b2):
    b1.config(text="")
    b2.config(text="")

for i, v in enumerate(values):
    b = tk.Button(root, text="", width=5, height=2)
    b.config(command=lambda btn=b, val=v: click(btn, val))
    b.grid(row=i//4, column=i%4)
    buttons.append(b)

root.mainloop()
