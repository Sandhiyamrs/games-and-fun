print("🐸 Frogger")

steps = 0
while steps < 3:
    move = input("Jump forward? (y/n): ")
    if move == "y":
        steps += 1
        print("Safe jump!")
    else:
        print("Hit by car 💥")
        break

if steps == 3:
    print("🎉 Frog crossed safely!")
