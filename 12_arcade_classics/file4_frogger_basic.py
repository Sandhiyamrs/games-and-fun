pos = 0
while pos < 5:
    move = input("Jump forward? (y): ")
    if move == 'y':
        pos += 1
        print("Frog at position:", pos)
print("🎉 You crossed the road!")
