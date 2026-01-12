sequence = ["do", "re", "mi"]
print("Remember this sequence:", sequence)
input("Press Enter to continue...")
guess = input("Enter sequence separated by space: ").split()

print("Correct!" if guess == sequence else "Wrong!")

