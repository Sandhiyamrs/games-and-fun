colors = ["Red", "Blue", "Green", "Yellow"]
import random

def color_game():
    while True:
        c = random.choice(colors)
        ans = input(f"Type this color exactly → {c}: ")
        if ans == c:
            print("✔ Correct!\n")
        else:
            print("❌ Try again.\n")

color_game()
