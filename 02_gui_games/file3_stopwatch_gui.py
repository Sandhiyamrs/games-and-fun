import tkinter as tk

running = False
counter = 0

def start():
    global running
    running = True
    update()

def stop():
    global running
    running = False

def reset():
    global counter
    counter = 0
    label.config(text="0")

def update():
    global counter
    if running:
        counter += 1
        label.config(text=str(counter))
        root.after(1000, update)

root = tk.Tk()
root.title("⏱ Stopwatch")

label = tk.Label(root, text="0", font=("Arial", 40))
label.pack()

tk.Button(root, text="Start", command=start).pack(fill="x")
tk.Button(root, text="Stop", command=stop).pack(fill="x")
tk.Button(root, text="Reset", command=reset).pack(fill="x")

root.mainloop()
