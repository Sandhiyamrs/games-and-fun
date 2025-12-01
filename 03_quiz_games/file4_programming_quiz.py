print("💻 Programming Quiz")

questions = {
    "What does HTML stand for? ": "hypertext markup language",
    "Which keyword is used to define a function in Python? ": "def",
    "What symbol is used for comments in Python? ": "#",
    "JavaScript runs in the browser: True or False? ": "true",
}

score = 0

for q, ans in questions.items():
    user = input(q).lower()
    if user == ans:
        print("✔ Correct!")
        score += 1
    else:
        print("✘ Wrong!")

print("\n🏆 Final Score:", score, "/", len(questions))
