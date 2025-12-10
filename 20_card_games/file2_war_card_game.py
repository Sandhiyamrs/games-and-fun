# Extremely simple war game for one round
import random
card_values = list(range(2,15))*4
random.shuffle(card_values)
p1=card_values.pop(); p2=card_values.pop()
print(f"Player1: {p1} vs Player2: {p2}")
if p1>p2: print("Player1 wins")
elif p2>p1: print("Player2 wins")
else: print("Tie - War!")

