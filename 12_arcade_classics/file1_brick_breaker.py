print("🧱 Brick Breaker (Text Version)")

bricks = 5
while bricks > 0:
    hit = input("Hit the ball? (y/n): ").lower()
    if hit == "y":
        bricks -= 1
        print(f"Brick broken! Remaining: {bricks}")
    else:
        print("Missed!")

print("🎉 All bricks cleared!")
