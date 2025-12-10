# Tiny virtual pet - very basic
import time

print("Welcome to TinyPet!")
hunger = 5  # 0 full - 10 very hungry

print("Your pet's hunger level:", hunger)
choice = input("Do you want to feed it? (y/n): ").strip().lower()
if choice == "y":
    hunger = max(0, hunger - 4)
    print("You fed your pet. Your pet is happy! ❤️")
else:
    hunger = min(10, hunger + 1)
    print("You did not feed your pet. It looks a bit sad.")
print("Hunger level now:", hunger)
time.sleep(0.5)

