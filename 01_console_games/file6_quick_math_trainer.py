import random

def math_trainer():
    score = 0
    for _ in range(5):
        a, b = random.randint(1,10), random.randint(1,10)
        answer = int(input(f"{a} + {b} = "))
        if answer == a + b:
            print("✔ Correct")
            score += 1
        else:
            print("✖ Wrong")

    print(f"Final Score: {score}/5")

if __name__ == "__main__":
    math_trainer()
