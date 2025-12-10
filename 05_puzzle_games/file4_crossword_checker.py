# Crossword Checker
solution = ["PYTHON", "GITHUB", "PUZZLE"]
user_input = [input(f"Word {i+1}: ").upper() for i in range(3)]

correct = sum([solution[i]==user_input[i] for i in range(3)])
print(f"Correct words: {correct}/3")
