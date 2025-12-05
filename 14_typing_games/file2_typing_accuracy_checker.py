text = "Python is super fun!"

print(text)
typed = input("\nType it exactly: ")

correct = sum(1 for a, b in zip(text, typed) if a == b)
accuracy = (correct / len(text)) * 100

print(f"Accuracy: {accuracy:.2f}%")
