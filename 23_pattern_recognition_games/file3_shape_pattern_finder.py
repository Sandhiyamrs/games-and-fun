# Simple shape pattern description
print("Square, triangle, square, triangle,... What comes next?")
ans = input("Your answer: ").strip().lower()
print("Correct!" if ans in ("square","square.") else "Expected 'square'")

