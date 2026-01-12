import random
p1 = random.randint(1,13)
p2 = random.randint(1,13)
print("Player 1:", p1, "Player 2:", p2)
print("Winner:", "P1" if p1 > p2 else "P2")
