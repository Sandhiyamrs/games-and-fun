def start():
    print("Welcome to the Haunted Mansion.")
    return {"health":10, "inventory":[], "visited":set()}

def foyer(state):
    print("\nFoyer: a grand door is behind you. Doors lead to library and dining room.")
    choice = input("[library]/[dining]/[exit]: ")
    if choice == "library":
        return "library"
    if choice == "dining":
        return "dining"
    if choice == "exit":
        return "leave"
    return "foyer"

def library(state):
    if "key" not in state["inventory"]:
        print("You find an old key between books.")
        state["inventory"].append("key")
    else:
        print("The library is dusty and empty.")
    return "foyer"

def dining(state):
    print("Dining room: a ghost appears!")
    choice = input("[hide]/[run]/[talk]: ")
    if choice == "hide":
        print("You hide successfully.")
        return "foyer"
    if choice == "run":
        state["health"] -= 3
        if state["health"] <= 0:
            return "dead"
        return "foyer"
    if choice == "talk" and "key" in state["inventory"]:
        print("Ghost calms; reveals secret basement.")
        return "basement"
    print("The ghost doesn't respond.")
    return "foyer"

def basement(state):
    print("Basement: Use key to open the chest? [yes/no]")
    c = input("> ")
    if c == "yes":
        print("You found treasure and freed the trapped spirit. You win!")
        return "win"
    return "foyer"

def play():
    state = start()
    loc = "foyer"
    while True:
        if loc == "foyer":
            loc = foyer(state)
        elif loc == "library":
            loc = library(state)
        elif loc == "dining":
            loc = dining(state)
        elif loc == "basement":
            loc = basement(state)
        elif loc == "leave":
            print("You left safely.")
            break
        elif loc == "dead":
            print("You were overwhelmed by the mansion. Game over.")
            break
        elif loc == "win":
            print("You solved the mystery! 🎉")
            break

if __name__ == "__main__":
    play()

