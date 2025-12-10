# Small grid memory: show positions with symbol, then hide
grid = [[".",".","."],[".",".","."],[".",".","."]]
grid[1][1]="X"
for row in grid:
    print(" ".join(row))
input("Memorize and press Enter...")
print("\n" * 40)
guess = input("Where was X? (row,col): ")
print("Correct!" if guess.strip()=="1,1" else "Nope, it was 1,1")

