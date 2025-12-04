import random
import time

def make_question(level=1):
    if level == 1:
        a, b = random.randint(1,10), random.randint(1,10)
        op = random.choice(['+','-'])
    else:
        a, b = random.randint(2,20), random.randint(2,12)
        op = random.choice(['+','-','*'])
    expr = f"{a}{op}{b}"
    return expr, eval(expr)

def math_speed_test(duration=30):
    start = time.time()
    correct = 0
    total = 0
    level = 1
    while time.time() - start < duration:
        expr, ans = make_question(level)
        print("Solve:", expr)
        try:
            user = input("> ")
            if time.time() - start >= duration:
                break
            if int(user) == ans:
                correct += 1
                print("✔")
            else:
                print(f"✘ (ans {ans})")
            total += 1
        except:
            print("Invalid")
        if correct >= 5:
            level = 2
    print(f"Time up! Score: {correct}/{total}")

if __name__ == "__main__":
    math_speed_test(30)

