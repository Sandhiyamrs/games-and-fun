score = 0
ans = input("If 2+2=4, 3+3=? ")
if ans=="6": score += 1
ans = input("If 5-2=?, ")
if ans=="3": score += 1
print(f"Total Score: {score}/2")
