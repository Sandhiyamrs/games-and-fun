import random
import time

score = 0
start_time = time.time()

print("➕ Math Speed Test\n")

for _ in range(5):
    a, b = random.randint(1, 20), random.randint(1, 20)
    answer = int(input(f"{a} + {b} = "))
    if answer == a + b:
        score += 1

end_time = time.time()

print(f"\nScore: {score}/5")
print(f"Time Taken: {end_time - start_time:.2f} seconds")
