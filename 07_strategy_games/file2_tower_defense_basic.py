base_health = 100
enemy_health = 30

print("🏰 Tower Defense Simulation\n")

for wave in range(1, 6):
    print(f"Wave {wave} incoming!")

    while enemy_health > 0:
        enemy_health -= 10
        print("Tower attacks! Enemy HP:", enemy_health)

    print("Enemy defeated!\n")
    enemy_health = 30
    base_health -= 5

print("Game Over | Base Health:", base_health)

