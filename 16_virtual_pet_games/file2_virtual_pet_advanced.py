# Virtual pet with simple stats and actions
import random
import time

pet = {"name": "Buddy", "hunger": 5, "happiness": 5, "energy": 5}

def status():
    print(f"{pet['name']} — Hunger:{pet['hunger']} Happiness:{pet['happiness']} Energy:{pet['energy']}")

def feed():
    pet["hunger"] = max(0, pet["hunger"] - 3)
    pet["happiness"] += 1
    print("You gave food. Yum!")

def play():
    if pet["energy"] >= 2:
        pet["happiness"] += 2
        pet["energy"] -= 2
        print("You played together! 🎾")
    else:
        print("Too tired to play.")

def rest():
    pet["energy"] = min(10, pet["energy"] + 3)
    print("Pet rested and regained energy.")

print("Virtual Pet Advanced")
for _ in range(3):
    status()
    action = input("Action (feed/play/rest): ").strip().lower()
    if action == "feed": feed()
    elif action == "play": play()
    elif action == "rest": rest()
    else: print("Nothing done.")
    # natural decay
    pet["hunger"] = min(10, pet["hunger"] + 1)
    time.sleep(0.3)
status()

