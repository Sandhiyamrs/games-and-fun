energy = 5
hunger = 5

while energy > 0 and hunger > 0:
    print(f"Energy: {energy}, Hunger: {hunger}")
    choice = input("feed / play / rest: ")

    if choice == "feed":
        hunger -= 1
    elif choice == "play":
        energy -= 1
        hunger += 1
    elif choice == "rest":
        energy += 1

print("Game Over!")
