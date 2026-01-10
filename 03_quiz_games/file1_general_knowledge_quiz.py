def run_quiz():
    questions = {
        "What is the capital of India? ": "delhi",
        "Which planet is known as the Red Planet? ": "mars",
        "Who wrote the national anthem of India? ": "tagore"
    }

    score = 0
    print("🧠 General Knowledge Quiz\n")

    for q, a in questions.items():
        user = input(q).strip().lower()
        if user == a:
            print("✅ Correct\n")
            score += 1
        else:
            print(f"❌ Wrong (Answer: {a})\n")

    print(f"Final Score: {score}/{len(questions)}")

run_quiz()
