import tkinter as tk
import random

a, b = random.randint(1, 10), random.randint(1, 10)

def check():
    try:
        if int(ans.get()) == a + b:
            result.set("✔ Correct!")
        else:
            result.set("❌ Wrong!")
    except:
        result.set("Enter a number")

root = tk.Tk()
root.title("Quick Math Trainer")

tk.Label(root, text=f"{a} + {b} = ?").pack()
ans = tk.Entry(root)
ans.pack()

tk.Button(root, text="Submit", command=check).pack()
result = tk.StringVar()
tk.Label(root, textvariable=result).pack()

root.mainloop()
