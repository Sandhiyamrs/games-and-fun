def print_board(board):
    print("\n")
    for i in range(0, 9, 3):
        print(" | ".join(board[i:i+3]))
        if i < 6:
            print("-" * 9)

def check_winner(board, player):
    win_combos = [
        (0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6)
    ]
    return any(all(board[i] == player for i in combo) for combo in win_combos)

def tic_tac_toe():
    board = [str(i+1) for i in range(9)]
    player = "X"

    for _ in range(9):
        print_board(board)
        move = input(f"Player {player}, choose position (1-9): ")

        if move.isdigit() and board[int(move)-1] not in ["X","O"]:
            board[int(move)-1] = player
        else:
            print("Invalid move!")
            continue

        if check_winner(board, player):
            print_board(board)
            print(f"🎉 Player {player} wins!")
            return

        player = "O" if player == "X" else "X"

    print_board(board)
    print("🤝 It's a draw!")

if __name__ == "__main__":
    tic_tac_toe()
