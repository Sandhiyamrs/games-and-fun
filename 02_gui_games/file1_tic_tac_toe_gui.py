# Tic-Tac-Toe GUI using Tkinter
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Tic-Tac-Toe GUI")

turn = "X"
buttons = [None]*9

def check_winner():
    wins = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    for a,b,c in wins:
        if buttons[a]["text"] == buttons[b]["text"] == buttons[c]["text"] != "":
            messagebox.showinfo("Winner", f"Player {buttons[a]['text']} wins!")
            root.quit()

def click(i):
    global turn
    if buttons[i]["text"] == "":
        buttons[i]["text"] = turn
        check_winner()
        turn = "O" if turn=="X" else "X"

frame = tk.Frame(root)
frame.pack()
for i in range(9):
    buttons[i] = tk.Button(frame, text="", font=("Arial",20), width=5, height=2, command=lambda i=i: click(i))
    buttons[i].grid(row=i//3, column=i%3)

root.mainloop()

