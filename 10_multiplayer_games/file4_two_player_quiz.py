questions = {"2+2":4,"5+3":8}
scores = [0,0]

for i in range(2):
    for q,a in questions.items():
        if int(input(f"Player {i+1}: {q} = ")) == a:
            scores[i]+=1

print("Scores:", scores)
