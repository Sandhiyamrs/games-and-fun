import random
import time

def ask_question(level=1):
    if level==1:
        a,b = random.randint(1,10), random.randint(1,10)
        op = random.choice(['+','-'])
    else:
        a,b = random.randint(2,20), random.randint(2,12)
        op = random.choice(['+','-','*'])
    q = f"{a}{op}{b}"
    return q, eval(q)

def round_duel(level=1):
    q, ans = ask_question(level)
    print("Solve:", q)
    t0 = time.time()
    p1 = input("Player1 answer: ")
    t1 = time.time()
    p2 = input("Player2 answer: ")
    t2 = time.time()
    try:
        p1 = int(p1)
    except:
        p1 = None
    try:
        p2 = int(p2)
    except:
        p2 = None

    # determine correctness and times
    r1 = (p1 == ans)
    r2 = (p2 == ans)
    if r1 and not r2:
        return 1
    if r2 and not r1:
        return 2
    if r1 and r2:
        # faster wins
        return 1 if (t1-t0) < (t2-t1) else 2
    return 0  # nobody

def play(target=3):
    score = {1:0, 2:0}
    level = 1
    while max(score.values()) < target:
        winner = round_duel(level)
        if winner == 0:
            print("No correct answers.")
        else:
            print(f"Player {winner} wins the round.")
            score[winner] += 1
        print("Score:", score)
    print("Match over!")

if __name__ == "__main__":
    play(3)

