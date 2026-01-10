logos = {
    "Apple logo belongs to which company? ": "apple",
    "Windows logo belongs to? ": "microsoft",
    "Play button logo? ": "youtube"
}

score = 0
print("🖼️ Logo Guess Quiz\n")

for q, a in logos.items():
    if input(q).lower() == a:
        score += 1

print(f"Score: {score}/{len(logos)}")
