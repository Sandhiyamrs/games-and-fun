import random

WORDS = ["python", "logic", "function", "variable"]

def scramble(word):
    return "".join(random.sample(word, len(word)))

def play():
    word = random.choice(WORDS)
    scrambled = scramble(word)

    print(f"Scrambled word: {scrambled}")
    guess = input("Guess the word: ")

    if guess == word:
        print("🎉 Correct!")
    else:
        print(f"❌ Wrong! Word was: {word}")

if __name__ == "__main__":
    play()
