height = 100
gravity = 9.8

print("⚽ Gravity Simulation\n")
while height > 0:
    height -= gravity
    print("Ball height:", max(0, int(height)))
