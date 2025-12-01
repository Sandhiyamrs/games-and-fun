import random
import time

cards = ["A", "A", "B", "B", "C", "C"]
random.shuffle(cards)

print("🧠 Memory Match Game!")
print("There are 6 cards (positions 1 to 6). Try to find pairs.\n")

revealed = ["*", "*", "*", "*", "*", "*"]
attempts = 0

while "*" in revealed:
    print("\nCards:", " ".join(revealed))
    
    first = int(input("Pick first card (1-6): ")) - 1
    second = int(input("Pick second card (1-6): ")) - 1

    attempts += 1

    if cards[first] == cards[second]:
        print("✔ Matched:", cards[first])
        revealed[first] = cards[first]
        revealed[second] = cards[second]
    else:
        print("❌ No Match")
        time.sleep(1)

print("\n🎉 You matched all cards in", attempts, "attempts!")
