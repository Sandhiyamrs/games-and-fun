import random

def game():
    choices = ["rock", "paper", "scissors"]
    computer = random.choice(choices)

    user = input("Choose rock / paper / scissors: ").lower()

    if user not in choices:
        print("Invalid choice!")
        return

    print(f"Computer chose: {computer}")

    if user == computer:
        print("🤝 Draw")
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        print("🎉 You win!")
    else:
        print("💻 Computer wins!")

if __name__ == "__main__":
    game()
