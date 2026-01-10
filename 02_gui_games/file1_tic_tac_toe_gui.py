import tkinter as tk

root = tk.Tk()
root.title("Tic Tac Toe")

buttons = []
player = "X"

def click(btn):
    global player
    if btn["text"] == "":
        btn["text"] = player
        player = "O" if player == "X" else "X"

for i in range(9):
    btn = tk.Button(root, text="", font=("Arial", 20), width=5, height=2)
    btn.config(command=lambda b=btn: click(b))
    btn.grid(row=i//3, column=i%3)
    buttons.append(btn)

root.mainloop()
