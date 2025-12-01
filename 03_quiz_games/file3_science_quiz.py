print("🔬 Science Quiz")

questions = {
    "What planet is known as the Red Planet? ": "mars",
    "What gas do plants produce during photosynthesis? ": "oxygen",
    "What is the speed of light? (in km/s) ": "300000",
    "What is H2O commonly known as? ": "water",
}

score = 0

for q, ans in questions.items():
    user = input(q).lower()
    if user == ans:
        print("✔ Correct!")
        score += 1
    else:
        print("✘ Wrong!")

print("\n🎯 Your Score:", score, "/", len(questions))
