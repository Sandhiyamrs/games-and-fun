import random

def brick_breaker():
    bricks = ["🟥", "🟧", "🟨", "🟩", "🟦"]
    print("BREAK THE BRICKS!\n")
    for i in range(5):
        row = "".join(random.choice(bricks) for _ in range(20))
        print(row)

brick_breaker()
