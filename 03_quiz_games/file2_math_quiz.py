import random

score = 0
print("➕ Math Quiz\n")

for _ in range(5):
    a, b = random.randint(1, 10), random.randint(1, 10)
    ans = int(input(f"{a} + {b} = "))
    if ans == a + b:
        print("✅ Correct\n")
        score += 1
    else:
        print("❌ Wrong\n")

print(f"Your Score: {score}/5")
