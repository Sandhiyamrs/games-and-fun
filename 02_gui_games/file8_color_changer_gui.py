import tkinter as tk
import random

colors = ["red", "blue", "green", "yellow", "purple", "orange"]

def change_color():
    root.configure(bg=random.choice(colors))

root = tk.Tk()
root.title("Color Changer")
root.geometry("300x200")

tk.Button(root, text="Change Color", command=change_color).pack(expand=True)

root.mainloop()
