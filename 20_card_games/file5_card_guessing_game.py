import random
card = random.randint(1,13)
guess = int(input("Guess card number: "))
print("Correct!" if guess == card else "Wrong!")
