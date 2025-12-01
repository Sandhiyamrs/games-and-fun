import random

words = ["python", "developer", "hangman", "programming", "computer"]

word = random.choice(words)
guessed = ["_"] * len(word)
attempts = 6

print("🎯 Welcome to Hangman!")

while attempts > 0:
    print("\nWord:", " ".join(guessed))
    guess = input("Enter a letter: ").lower()

    if guess in word:
        print("✔ Correct!")
        for i in range(len(word)):
            if word[i] == guess:
                guessed[i] = guess
    else:
        attempts -= 1
        print(f"❌ Wrong! Attempts left: {attempts}")

    if "_" not in guessed:
        print("\n🎉 You win! The word was:", word)
        break
else:
    print("\n💀 You lost! The word was:", word)
