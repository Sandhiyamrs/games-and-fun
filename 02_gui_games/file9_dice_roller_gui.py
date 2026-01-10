import tkinter as tk
import random

def roll():
    result.set(f"🎲 Dice Roll: {random.randint(1, 6)}")

root = tk.Tk()
root.title("Dice Roller")

tk.Button(root, text="Roll Dice", command=roll).pack(pady=10)
result = tk.StringVar()
tk.Label(root, textvariable=result, font=("Arial", 16)).pack()

root.mainloop()
