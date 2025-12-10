# Very simple AI using random valid moves (not optimal)
import random

board = [" "]*9
def printb():
    for r in range(3):
        print(board[r*3:(r+1)*3])
def win(p):
    wins = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    return any(all(board[i]==p for i in w) for w in wins)

print("AI Tic-Tac-Toe (you = X, ai = O)")
while True:
    printb()
    move = int(input("Your move (0-8): "))
    if board[move]!=" ": continue
    board[move]="X"
    if win("X"):
        printb(); print("You win!"); break
    avail = [i for i,v in enumerate(board) if v==" "]
    if not avail:
        print("Draw"); break
    ai = random.choice(avail)
    board[ai]="O"
    if win("O"):
        printb(); print("AI wins!"); break

