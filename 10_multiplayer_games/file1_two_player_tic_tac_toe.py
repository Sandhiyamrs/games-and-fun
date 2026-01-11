board = [" "] * 9

def show():
    for i in range(0, 9, 3):
        print(board[i:i+3])

player = "X"
for _ in range(9):
    show()
    move = int(input(f"Player {player} move (0-8): "))
    if board[move] == " ":
        board[move] = player
        player = "O" if player == "X" else "X"
show()

