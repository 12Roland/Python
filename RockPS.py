# Rock Paper Scissors in python
import random

def play():
    print("=== Rock, Paper, Scissors Game ===")
    print("Type 'rock', 'paper', or 'scissors' to play. Type 'q' to quit.")

    choices = ["rock", "paper", "scissors"]

    while True:
        user = input("\nYour choice: ").lower()
        if user == 'q':
            print("Thanks for playing! 👋")
            break

        if user not in choices:
            print("Invalid choice! Please type rock, paper, or scissors.")
            continue

        computer = random.choice(choices)
        print(f"Computer chose: {computer}")

        if user == computer:
            print("It's a tie! 🤝")
        elif (user == "rock" and computer == "scissors") or \
             (user == "scissors" and computer == "paper") or \
             (user == "paper" and computer == "rock"):
            print("🎉 You win!")
        else:
            print("😢 You lose!")

if __name__ == "__main__":
    play()
