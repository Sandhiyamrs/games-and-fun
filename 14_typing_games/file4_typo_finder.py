original = "programming"
typed = input("Type 'programming': ")

for i,(o,t) in enumerate(zip(original, typed)):
    if o != t:
        print(f"Typo at position {i}")
