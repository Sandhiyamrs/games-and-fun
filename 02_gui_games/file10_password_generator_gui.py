import tkinter as tk
import random
import string

def generate():
    length = int(entry.get())
    chars = string.ascii_letters + string.digits + string.punctuation
    pwd.set("".join(random.choice(chars) for _ in range(length)))

root = tk.Tk()
root.title("Password Generator")

tk.Label(root, text="Password Length").pack()
entry = tk.Entry(root)
entry.pack()

tk.Button(root, text="Generate", command=generate).pack()
pwd = tk.StringVar()
tk.Entry(root, textvariable=pwd, width=30).pack()

root.mainloop()
