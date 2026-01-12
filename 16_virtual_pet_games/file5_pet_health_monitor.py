health = 100

while health > 0:
    damage = int(input("Health damage (0 to stop): "))
    if damage == 0:
        break
    health -= damage
    print("Health:", health)

print("Health check complete.")
