low, high = 1, 100
while low <= high:
    mid = (low + high) // 2
    response = input(f"Is it {mid}? (h/l/c): ")
    if response == "c":
        print("AI guessed it!")
        break
    elif response == "h":
        high = mid - 1
    else:
        low = mid + 1

