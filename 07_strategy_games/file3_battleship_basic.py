grid = [["~"] * 5 for _ in range(5)]
ship_position = (2, 3)

print("🚢 Battleship Game\n")

guess = (int(input("Row: ")), int(input("Column: ")))

if guess == ship_position:
    print("Hit! 💥 Ship destroyed!")
else:
    print("Miss! 🌊")
