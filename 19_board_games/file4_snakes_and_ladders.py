print("Othello starting board")
board = [["." for _ in range(8)] for _ in range(8)]
board[3][3] = "W"
board[4][4] = "W"
board[3][4] = "B"
board[4][3] = "B"
for r in board:
    print(" ".join(r))
