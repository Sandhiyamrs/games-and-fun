import random
import time

sequence = [random.randint(1, 9) for _ in range(5)]
print("🧠 Memory Booster Game\n")
print("Memorize this sequence:")
print(sequence)

time.sleep(3)
print("\n" * 30)

user_input = input("Enter the numbers in order (space-separated): ").split()

if user_input == list(map(str, sequence)):
    print("🎉 Excellent Memory!")
else:
    print("❌ Incorrect!")
    print("Correct sequence was:", sequence)
