import random

words = ["python", "computer", "programming", "puzzle", "gaming", "science"]

word = random.choice(words)
scrambled = "".join(random.sample(word, len(word)))

print("🔤 Word Scramble Game!")
print("Unscramble this word:", scrambled)

guess = input("Your guess: ")

if guess.lower() == word:
    print("🎉 Correct! You solved it!")
else:
    print(f"❌ Wrong! The correct word was: {word}")
