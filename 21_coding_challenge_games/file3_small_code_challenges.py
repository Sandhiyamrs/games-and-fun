# Three mini code puzzles
puzzles = [
    ("Reverse string 'hello'", "olleh"),
    ("2**3", "8"),
    ("len('abc')", "3")
]
score=0
for q,ans in puzzles:
    user=input(q+" = ")
    if user.strip()==ans: score+=1
print("Score:", score, "/", len(puzzles))
