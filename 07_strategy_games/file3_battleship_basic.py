import random
board = ["~"]*5
ship = random.randint(0,4)
guess = int(input("Guess the ship position (0-4): "))
if guess == ship: print("Hit! 🎯")
else: print(f"Miss! Ship was at {ship}")
