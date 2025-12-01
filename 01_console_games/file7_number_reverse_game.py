print("🔢 Number Reverse Game")

num = input("Enter a number: ")

if num.isdigit():
    reversed_num = num[::-1]
    print("Reversed number:", reversed_num)
else:
    print("❌ Invalid input! Enter digits only.")
