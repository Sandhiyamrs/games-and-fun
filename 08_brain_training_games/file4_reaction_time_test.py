import time
import random

print("⚡ Reaction Time Test")
print("Wait for GO...")

time.sleep(random.randint(2, 5))
print("GO!")

start = time.time()
input()
end = time.time()

print(f"Your Reaction Time: {end - start:.3f} seconds")
