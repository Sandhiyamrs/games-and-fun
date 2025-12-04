def intro():
    print("You wake up in a dim cockpit of a derelict spaceship.")
    print("Your goal: find the escape pod and survive.")
    return {"health":10, "inventory":[], "location":"cockpit"}

def cockpit(state):
    print("\nCockpit: you see corridors left and right, and a hatch to the engine room.")
    choice = input("Go [left]/[right]/[engine]: ")
    if choice == "left":
        return "cargo"
    if choice == "right":
        return "medbay"
    if choice == "engine":
        return "engine"
    return "cockpit"

def cargo(state):
    print("Cargo: you find a medkit.")
    if "medkit" not in state["inventory"]:
        state["inventory"].append("medkit")
        print("Picked medkit.")
    return "corridor"

def medbay(state):
    print("Medbay: a sleeping alien! Sneak or fight?")
    choice = input("[sneak]/[fight]: ")
    if choice == "sneak":
        print("You sneak past.")
        return "escape_hatch"
    else:
        print("Alien wakes up, you fight and get hurt.")
        state["health"] -= 5
        if state["health"] <= 0:
            return "dead"
        return "corridor"

def engine(state):
    print("Engine: alarms blare. You can try to repair or flee.")
    choice = input("[repair]/[flee]: ")
    if choice == "repair":
        print("You repair engine and unlock escape pod.")
        return "escape_hatch"
    return "corridor"

def corridor(state):
    print("Corridor: leads to escape hatch or cockpit.")
    choice = input("[escape]/[cockpit]: ")
    if choice == "escape":
        if "medkit" in state["inventory"]:
            print("You used medkit to patch yourself and jump into escape pod.")
            return "escaped"
        else:
            print("You are wounded and can't reach pod.")
            return "dead"
    return "cockpit"

def play():
    state = intro()
    loc = "cockpit"
    while True:
        if loc == "cockpit":
            loc = cockpit(state)
        elif loc == "cargo":
            loc = cargo(state)
        elif loc == "medbay":
            loc = medbay(state)
        elif loc == "engine":
            loc = engine(state)
        elif loc == "corridor":
            loc = corridor(state)
        elif loc == "escape_hatch" or loc == "escaped":
            print("You escaped! 🎉")
            break
        elif loc == "dead":
            print("You died. Game over.")
            break

if __name__ == "__main__":
    play()

