import random

words = ["python", "gaming", "fun", "terminal", "coding"]

word = random.choice(words)
scrambled = "".join(random.sample(word, len(word)))

print("🔀 Word Scramble Game")
print("Scrambled word:", scrambled)

guess = input("Your guess: ")

if guess == word:
    print("🎉 Correct!")
else:
    print("❌ Wrong! The word was:", word)
