# Simple chatbot that asks quiz questions and responds
qa = [("Capital of France?","paris"),("2+2?","4")]
print("QuizBot: I will ask questions.")
score=0
for q,a in qa:
    ans = input("QuizBot: "+q+" ").strip().lower()
    if ans==a:
        print("QuizBot: Correct!")
        score+=1
    else:
        print("QuizBot: Nope.")
print(f"QuizBot: Your score {score}/{len(qa)}")

