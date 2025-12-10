# Tiny connect-four single-column drop play for demo
rows, cols = 6,7
board = [[" "]*cols for _ in range(rows)]
def printb():
    for r in board:
        print("|".join(r))
print("Connect Four (demo). Players alternate placing at col index.")
turn = "X"
for _ in range(8):
    printb()
    c = int(input(f"Player {turn} column (0-{cols-1}): "))
    for r in reversed(range(rows)):
        if board[r][c]==" ":
            board[r][c]=turn
            break
    turn = "O" if turn=="X" else "X"
print("Demo ended.")

