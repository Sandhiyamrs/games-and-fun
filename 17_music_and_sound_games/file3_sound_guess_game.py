# Simple text-based 'sound' guessing game using hints
hints = [
    ("A tick-tock clock", "clock"),
    ("A barking animal", "dog"),
    ("A bright ringing bell", "bell"),
]
print("Sound Guess Game")
for hint, ans in hints:
    guess = input(f"Hint: {hint}. Your guess: ").strip().lower()
    print("Correct!" if guess == ans else f"Incorrect! It was {ans}")

