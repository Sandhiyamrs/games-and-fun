# Show a short sequence to memorize
import random, time
seq = [random.randint(0,9) for _ in range(5)]
print("Memorize this:", " ".join(map(str,seq)))
time.sleep(3)
print("\n" * 40)
ans = input("Enter the sequence: ").strip().split()
print("Correct!" if list(map(str,seq))==ans else "Wrong. Was: "+" ".join(map(str,seq)))

