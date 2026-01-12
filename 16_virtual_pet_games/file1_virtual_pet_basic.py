pet_name = input("Name your pet: ")
hunger = 5

print(f"{pet_name} is born!")

while hunger > 0:
    action = input("Feed pet? (y/n): ").lower()
    if action == "y":
        hunger -= 1
        print("Pet is happier 😊")
    else:
        hunger += 1
        print("Pet is getting hungry 😢")

print(f"{pet_name} is fully satisfied!")
