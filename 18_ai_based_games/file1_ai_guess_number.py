# AI tries to guess your number using binary search
low, high = 1, 100
print("Think of a number between 1 and 100. I will guess.")
while low <= high:
    mid = (low + high) // 2
    ans = input(f"My guess is {mid}. Is it 'higher', 'lower', or 'correct'? ").strip().lower()
    if ans == "correct":
        print("Yay! I guessed it.")
        break
    elif ans == "higher":
        low = mid + 1
    elif ans == "lower":
        high = mid - 1
    else:
        print("Please answer: higher/lower/correct.")

