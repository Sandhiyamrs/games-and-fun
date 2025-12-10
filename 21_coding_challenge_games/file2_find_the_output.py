# Show a small code snippet and ask what it prints
snippet = "a = [1,2,3]\nprint(a[::-1])"
print("What is the output of:\n", snippet)
user = input("Your guess: ").strip()
print("Correct answer: [3, 2, 1]. You answered:", user)

