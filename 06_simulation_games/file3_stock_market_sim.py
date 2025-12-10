import random
price = 100
for day in range(1,6):
    change = random.randint(-10,10)
    price += change
    print(f"Day {day}: ${price}")
