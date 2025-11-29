# Rock Paper Scissors

import random

options = ["rock", "paper", "scissors"]

while True:
    user_choice = input("Enter rock, paper, or scissors (or quit to exit): ").lower()
    if user_choice == "quit":
        break
    if user_choice not in options:
        print("Invalid choice!")
        continue

    comp_choice = random.choice(options)
    print(f"Computer chose: {comp_choice}")

    if user_choice == comp_choice:
        print("It's a tie!")
    elif (user_choice=="rock" and comp_choice=="scissors") or \
         (user_choice=="paper" and comp_choice=="rock") or \
         (user_choice=="scissors" and comp_choice=="paper"):
        print("You win!")
    else:
        print("You lose!")

