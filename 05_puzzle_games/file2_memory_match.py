import random

numbers = [1,2,3,4,5]
random.shuffle(numbers)
print("Memorize:", numbers)
input("Press Enter to hide...")
print("\n" * 20)

guess = input("Enter numbers in order: ").split()
if guess == list(map(str, numbers)):
    print("🎉 Correct!")
else:
    print("❌ Wrong!")
