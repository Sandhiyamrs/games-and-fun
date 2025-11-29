# General Knowledge Quiz
questions = {
    "Capital of France?": "Paris",
    "Largest ocean?": "Pacific",
    "Fastest land animal?": "Cheetah"
}

score = 0
for q,a in questions.items():
    ans = input(q + " ")
    if ans.strip().lower() == a.lower():
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! Answer: {a}")
print(f"Your score: {score}/{len(questions)}")

