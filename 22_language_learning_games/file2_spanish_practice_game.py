# Spanish practice
pairs = {"hola":"hello","gracias":"thank you"}
for s,e in pairs.items():
    ans = input(f"Translate '{s}' to English: ").strip().lower()
    print("Correct!" if ans==e else f"Wrong. Answer: {e}")

