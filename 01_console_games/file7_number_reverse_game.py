def reverse_game():
    num = input("Enter a number: ")
    if num.isdigit():
        print("Reversed:", num[::-1])
    else:
        print("Invalid input!")

if __name__ == "__main__":
    reverse_game()
