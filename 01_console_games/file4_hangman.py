import random

WORDS = ["python", "developer", "hangman", "programming"]

def hangman():
    word = random.choice(WORDS)
    guessed = set()
    attempts = 6

    while attempts > 0:
        display = [c if c in guessed else "_" for c in word]
        print("Word:", " ".join(display))

        if "_" not in display:
            print("🎉 You guessed the word!")
            return

        guess = input("Guess a letter: ").lower()

        if guess in guessed:
            print("Already guessed!")
            continue

        guessed.add(guess)

        if guess not in word:
            attempts -= 1
            print(f"Wrong! Attempts left: {attempts}")

    print(f"💀 Game Over! Word was: {word}")

if __name__ == "__main__":
    hangman()
