# Show random shuffle of 5 cards
import random
deck = list(range(1,53))
random.shuffle(deck)
print("Top 5 cards after shuffle:", deck[:5])

