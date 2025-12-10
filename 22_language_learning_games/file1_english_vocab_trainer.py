# English vocab trainer (simple)
words = {"benevolent":"kind and well-meaning","gregarious":"sociable"}
for w, m in words.items():
    ans = input(f"Meaning of {w}: ").strip().lower()
    print("Correct!" if ans in m else f"Answer: {m}")

