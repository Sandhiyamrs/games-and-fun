import tkinter as tk
import random

number = random.randint(1, 100)
attempts = 0

def check_guess():
    global attempts
    try:
        guess = int(entry.get())
        attempts += 1
        if guess < number:
            result.set("Too Low ⬇️")
        elif guess > number:
            result.set("Too High ⬆️")
        else:
            result.set(f"🎉 Correct! Attempts: {attempts}")
    except ValueError:
        result.set("Enter a valid number")

root = tk.Tk()
root.title("Number Guess Game")

tk.Label(root, text="Guess a number (1–100)").pack()
entry = tk.Entry(root)
entry.pack()

tk.Button(root, text="Check", command=check_guess).pack()

result = tk.StringVar()
tk.Label(root, textvariable=result, font=("Arial", 14)).pack()

root.mainloop()
