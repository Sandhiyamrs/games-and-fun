# Math Quiz
import random

score = 0
for i in range(5):
    a = random.randint(1,20)
    b = random.randint(1,20)
    ans = int(input(f"{a} + {b} = "))
    if ans == a+b:
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! Answer: {a+b}")
print(f"Your score: {score}/5")

