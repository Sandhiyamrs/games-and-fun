word = "python"
guess = input("Enter crossword word: ")

if guess.lower() == word:
    print("✅ Correct!")
else:
    print("❌ Incorrect!")
