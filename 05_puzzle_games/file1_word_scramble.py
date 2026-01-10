import random

word = random.choice(["python", "developer", "challenge"])
scrambled = ''.join(random.sample(word, len(word)))

print("Scrambled Word:", scrambled)
guess = input("Your guess: ")

if guess == word:
    print("✅ Correct!")
else:
    print("❌ Wrong! Word was:", word)
