# Pet feeding simulator (counts meals)
meals = 0
print("Pet Feeding Simulator")
while True:
    cmd = input("Type 'feed' to feed, 'status' or 'quit': ").strip().lower()
    if cmd == "feed":
        meals += 1
        print(f"Fed pet. Meals given: {meals}")
    elif cmd == "status":
        print(f"Meals so far: {meals}")
    elif cmd == "quit":
        print("Goodbye!")
        break
    else:
        print("Unknown command.")

