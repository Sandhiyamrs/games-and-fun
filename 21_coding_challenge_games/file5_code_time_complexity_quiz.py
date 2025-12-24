print("⏱️ Time Complexity Quiz")

question = "What is the time complexity of binary search?"
answer = input("Your answer: ")

if answer.lower() in ["o(log n)", "log n"]:
    print("✅ Correct!")
else:
    print("❌ Incorrect. Correct answer: O(log n)")
