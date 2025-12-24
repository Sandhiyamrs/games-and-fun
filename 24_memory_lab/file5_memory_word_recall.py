import time

words = ["apple", "river", "cloud"]
print("Remember these words:", words)

time.sleep(4)
print("\n" * 50)

recall = input("Enter the words: ")

print("Original:", words)
print("Your Recall:", recall.split())
