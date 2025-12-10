# Very simple Ludo dice mover for one token
position = 0
print("Ludo Simulator")
for i in range(5):
    input("Press Enter to roll dice")
    import random
    roll=random.randint(1,6)
    position+=roll
    print(f"Rolled {roll}. New position: {position}")

