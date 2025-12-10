import random
board = [" "] * 9
def print_board(): print(board[0:3], board[3:6], board[6:9])
for i in range(5):
    player = int(input("Your move (0-8): "))
    board[player] = "X"
    ai = random.choice([i for i in range(9) if board[i]==" "])
    board[ai] = "O"
    print_board()
