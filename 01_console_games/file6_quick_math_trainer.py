import random
import time

print("🧠 Quick Math Trainer")
score = 0

for _ in range(5):
    a = random.randint(1, 20)
    b = random.randint(1, 20)
    op = random.choice(["+", "-"])

    if op == "+":
        ans = a + b
    else:
        ans = a - b

    start = time.time()
    user = int(input(f"{a} {op} {b} = "))
    end = time.time()

    if user == ans and (end - start) <= 5:
        print("✔ Correct!")
        score += 1
    else:
        print("❌ Wrong or too slow!")

print("Your final score:", score)
