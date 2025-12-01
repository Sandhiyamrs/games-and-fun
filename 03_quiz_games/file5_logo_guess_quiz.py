print("🏪 Logo Guess Quiz")
print("Guess the brand based on the hint!\n")

questions = {
    "🔵 Blue circle logo with a white 'f' (social media)": "facebook",
    "🟡 Yellow 'M' fast-food brand": "mcdonalds",
    "🍎 Half-bitten apple logo": "apple",
    "▶️ Red play button video platform": "youtube",
}

score = 0

for hint, answer in questions.items():
    print("\nHint:", hint)
    user = input("Your answer: ").lower()

    if user == answer:
        print("✔ Correct!")
        score += 1
    else:
        print("✘ Wrong!")

print("\n🎉 Total Score:", score, "/", len(questions))
