import random

def game():
    target = random.randint(1, 100)
    print("Guess the number between 1 and 100!")

    while True:
        g = int(input("Your guess: "))
        if g == target:
            print("🎉 Correct!")
            break
        print("📉 Too low!" if g < target else "📈 Too high!")

game()
