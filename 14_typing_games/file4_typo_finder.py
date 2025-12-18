text = "pythno"
correct = "python"
print("Mistakes:", sum(a!=b for a,b in zip(text, correct)))
