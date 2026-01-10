import random

board = [" "] * 9

def print_board():
    for i in range(0, 9, 3):
        print(board[i:i+3])

def ai_move():
    choices = [i for i in range(9) if board[i] == " "]
    return random.choice(choices)

print("🤖 Tic Tac Toe vs AI\n")

for turn in range(5):
    print_board()
    move = int(input("Your move (0-8): "))
    board[move] = "X"

    ai = ai_move()
    board[ai] = "O"

print_board()
print("Game Finished")
