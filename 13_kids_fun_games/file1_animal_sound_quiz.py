sounds = {
    "Meow": "Cat",
    "Woof": "Dog",
    "Moo": "Cow",
    "Neigh": "Horse"
}

for sound, animal in sounds.items():
    guess = input(f"Which animal makes '{sound}'? ")
    print("Correct!\n" if guess.lower() == animal.lower() else f"Wrong! It is {animal}.\n")
