import math
import random

def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
    print("\n")

def available_moves(board):
    return [(r, c) for r in range(3) for c in range(3) if board[r][c] == " "]

def check_winner(board):
    wins = [
        [(0,0),(0,1),(0,2)], [(1,0),(1,1),(1,2)], [(2,0),(2,1),(2,2)],
        [(0,0),(1,0),(2,0)], [(0,1),(1,1),(2,1)], [(0,2),(1,2),(2,2)],
        [(0,0),(1,1),(2,2)], [(0,2),(1,1),(2,0)]
    ]
    for line in wins:
        values = [board[r][c] for r, c in line]
        if values == ["X","X","X"]: return "X"
        if values == ["O","O","O"]: return "O"
    return None

def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    if winner == "O": return 1
    if winner == "X": return -1
    if not available_moves(board): return 0

    if is_maximizing:
        best_score = -math.inf
        for r, c in available_moves(board):
            board[r][c] = "O"
            score = minimax(board, depth + 1, False)
            board[r][c] = " "
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for r, c in available_moves(board):
            board[r][c] = "X"
            score = minimax(board, depth + 1, True)
            board[r][c] = " "
            best_score = min(score, best_score)
        return best_score

def ai_move(board):
    best_score = -math.inf
    move = None
    for r, c in available_moves(board):
        board[r][c] = "O"
        score = minimax(board, 0, False)
        board[r][c] = " "
        if score > best_score:
            best_score = score
            move = (r, c)
    return move

def play():
    board = [[" "]*3 for _ in range(3)]
    print("Tic Tac Toe vs AI")

    while True:
        print_board(board)
        r = int(input("Enter row (0-2): "))
        c = int(input("Enter col (0-2): "))
        if board[r][c] != " ":
            print("Invalid move!")
            continue

        board[r][c] = "X"

        if check_winner(board) == "X":
            print_board(board)
            print("🎉 You Win!")
            break

        if not available_moves(board):
            print_board(board)
            print("Draw!")
            break

        print("AI thinking...")
        r, c = ai_move(board)
        board[r][c] = "O"

        if check_winner(board) == "O":
            print_board(board)
            print("💀 AI Wins!")
            break

play()

