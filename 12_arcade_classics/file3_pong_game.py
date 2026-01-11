print("🏓 Pong Game")

score = 0
for _ in range(5):
    move = input("Move paddle (left/right): ")
    if move in ["left", "right"]:
        score += 1

print("Final Score:", score)
