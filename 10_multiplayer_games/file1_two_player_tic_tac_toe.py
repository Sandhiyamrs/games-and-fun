def print_board(b):
    for row in b:
        print(" | ".join(row))
    print()

def check_win(b, mark):
    # rows, cols, diagonals
    for i in range(3):
        if all(b[i][j]==mark for j in range(3)): return True
        if all(b[j][i]==mark for j in range(3)): return True
    if b[0][0]==mark and b[1][1]==mark and b[2][2]==mark: return True
    if b[0][2]==mark and b[1][1]==mark and b[2][0]==mark: return True
    return False

def play_round():
    board = [[" "]*3 for _ in range(3)]
    current = "X"
    moves = 0
    while moves < 9:
        print_board(board)
        r,c = map(int, input(f"Player {current} move (r c): ").split())
        if board[r][c] != " ":
            print("Invalid move")
            continue
        board[r][c] = current
        moves += 1
        if check_win(board, current):
            print_board(board)
            print(f"Player {current} wins!")
            return current
        current = "O" if current == "X" else "X"
    print_board(board)
    print("Draw!")
    return None

def main():
    score = {"X":0, "O":0, "Draws":0}
    while True:
        winner = play_round()
        if winner is None:
            score["Draws"] += 1
        else:
            score[winner] += 1
        print("Score:", score)
        cont = input("Play again? (y/n): ")
        if cont.lower() != "y":
            break

if __name__ == "__main__":
    main()

