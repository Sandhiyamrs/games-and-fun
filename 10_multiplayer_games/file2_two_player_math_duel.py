import random

scores = {"P1":0, "P2":0}

for p in scores:
    a,b = random.randint(1,10), random.randint(1,10)
    ans = int(input(f"{p}: {a}+{b} = "))
    if ans == a+b:
        scores[p]+=1

print("Scores:", scores)

