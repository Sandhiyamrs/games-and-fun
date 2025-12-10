# Very simpel: show words then ask after a delay
import time
words = ["apple","book","car"]
print("Remember these words:", ", ".join(words))
time.sleep(2)
print("\n" * 40)
input("Press Enter to recall...")
for w in words:
    ans = input("One word: ").strip().lower()
    print("OK" if ans==w else f"Was {w}")
print("Done")

