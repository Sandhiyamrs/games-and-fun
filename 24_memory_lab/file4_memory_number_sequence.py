import time

sequence = [7, 2, 9, 4]
print("Memorize this sequence:", sequence)

time.sleep(3)
print("\n" * 50)

user = input("Enter the sequence: ")

if user == " ".join(map(str, sequence)):
    print("✅ Correct!")
else:
    print("❌ Incorrect")
