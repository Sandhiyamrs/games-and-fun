import tkinter as tk

root = tk.Tk()
root.title("🧮 Calculator")

expression = ""

def press(num):
    global expression
    expression += str(num)
    equation.set(expression)

def equal():
    global expression
    try:
        total = str(eval(expression))
        equation.set(total)
        expression = total
    except:
        equation.set("Error")
        expression = ""

def clear():
    global expression
    expression = ""
    equation.set("")

equation = tk.StringVar()
entry = tk.Entry(root, textvariable=equation, font=("Arial", 20), justify="right")
entry.grid(columnspan=4)

buttons = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
    ('0',4,0), ('.',4,1), ('=',4,2), ('+',4,3)
]

for (text,r,c) in buttons:
    if text == "=":
        tk.Button(root, text=text, width=5, command=equal).grid(row=r, column=c)
    else:
        tk.Button(root, text=text, width=5, command=lambda t=text: press(t)).grid(row=r, column=c)

tk.Button(root, text="Clear", width=20, command=clear).grid(row=5, columnspan=4)

root.mainloop()
