# Tic-Tac-Toe Game (Console)

board = [" "]*9

def show():
    print(board[0],"|",board[1],"|",board[2])
    print("--+---+--")
    print(board[3],"|",board[4],"|",board[5])
    print("--+---+--")
    print(board[6],"|",board[7],"|",board[8])

def check_winner(mark):
    wins = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    for c in wins:
        if board[c[0]]==board[c[1]]==board[c[2]]==mark:
            return True
    return False

turn = "X"
for i in range(9):
    show()
    pos = int(input(f"Player {turn}, choose (0-8): "))
    if board[pos] == " ":
        board[pos] = turn
    else:
        print("Already occupied! Try again.")
        continue

    if check_winner(turn):
        show()
        print(f"Player {turn} wins!")
        break

    turn = "O" if turn=="X" else "X"

