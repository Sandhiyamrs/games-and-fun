import random
import os
import time

def clear(): 
    os.system('cls' if os.name == 'nt' else 'clear')

def make_board(size=4):
    pairs = (size*size)//2
    values = list(range(1, pairs+1)) * 2
    random.shuffle(values)
    board = [values[i*size:(i+1)*size] for i in range(size)]
    revealed = [[False]*size for _ in range(size)]
    return board, revealed

def print_board(board, revealed):
    size = len(board)
    for r in range(size):
        row = []
        for c in range(size):
            if revealed[r][c]:
                row.append(str(board[r][c]).rjust(2))
            else:
                row.append("##")
        print(" ".join(row))
    print()

def play(size=4):
    board, revealed = make_board(size)
    moves = 0
    matches = 0
    while matches < (size*size)//2:
        clear()
        print_board(board, revealed)
        try:
            a = input("First card (r,c): ")
            r1,c1 = map(int, a.split(","))
            b = input("Second card (r,c): ")
            r2,c2 = map(int, b.split(","))
        except:
            print("Invalid input. Use r,c")
            time.sleep(1)
            continue
        if revealed[r1][c1] or revealed[r2][c2] or (r1==r2 and c1==c2):
            print("Invalid picks")
            time.sleep(1)
            continue
        moves += 1
        revealed[r1][c1] = True
        revealed[r2][c2] = True
        clear()
        print_board(board, revealed)
        if board[r1][c1] == board[r2][c2]:
            print("Match!")
            matches += 1
        else:
            print("No match.")
            time.sleep(1)
            revealed[r1][c1] = False
            revealed[r2][c2] = False
    print(f"Completed in {moves} moves!")

if __name__ == "__main__":
    play(4)

