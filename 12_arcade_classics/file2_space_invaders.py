print("👾 Space Invaders")

aliens = 3
while aliens > 0:
    action = input("Shoot or hide? ").lower()
    if action == "shoot":
        aliens -= 1
        print("Alien destroyed!")
    else:
        print("Alien attacks!")

print("🚀 Earth saved!")
