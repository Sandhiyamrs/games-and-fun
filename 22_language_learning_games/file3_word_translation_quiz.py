# Mixed translation quiz
qa = [("cat","gato"),("house","casa")]
score=0
for en,sp in qa:
    ans = input(f"Translate '{en}' to Spanish: ").strip().lower()
    if ans==sp: score+=1; print("✅")
    else: print("❌, correct:", sp)
print("Score:", score)

