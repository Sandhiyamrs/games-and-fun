questions = {
    "Water chemical formula? ": "h2o",
    "Gas used for breathing? ": "oxygen",
    "Center of atom is called? ": "nucleus"
}

score = 0
print("🔬 Science Quiz\n")

for q, a in questions.items():
    if input(q).lower() == a:
        score += 1
        print("✅ Correct\n")
    else:
        print(f"❌ Wrong (Answer: {a})\n")

print(f"Score: {score}/{len(questions)}")
