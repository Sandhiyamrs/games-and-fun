patterns = {
    "2, 4, 6, 8, ?" : "10",
    "3, 9, 27, ?" : "81",
    "1, 1, 2, 3, 5, ?" : "8"
}

for seq, ans in patterns.items():
    guess = input(f"Find the next number → {seq}: ")
    print("Correct!" if guess == ans else f"Wrong! Correct answer: {ans}")
