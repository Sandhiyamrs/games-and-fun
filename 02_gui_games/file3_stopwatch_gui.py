import tkinter as tk
import time

start_time = None
running = False

def start():
    global start_time, running
    start_time = time.time()
    running = True
    update()

def update():
    if running:
        elapsed = time.time() - start_time
        label.config(text=f"{elapsed:.2f}s")
        root.after(100, update)

root = tk.Tk()
label = tk.Label(root, text="0.00s", font=("Arial", 30))
label.pack()

tk.Button(root, text="Start", command=start).pack()
root.mainloop()
