import random

price = 100.0
print("📈 Stock Market Simulation\n")

for day in range(1, 8):
    change = random.uniform(-5, 5)
    price += change
    price = max(price, 1)
    print(f"Day {day}: Stock Price = ₹{price:.2f}")
