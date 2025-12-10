# A simple memory test for sequences (notes as letters)
import random

notes = ["A","B","C","D"]
seq = [random.choice(notes) for _ in range(3)]
print("Music Memory Game")
print("Memorize sequence:", " ".join(seq))
input("Press Enter when ready to hide...")
print("\n" * 40)
guess = input("Enter the sequence separated by space: ").strip().upper().split()
print("Correct!" if guess == seq else f"Wrong! It was: {' '.join(seq)}")

