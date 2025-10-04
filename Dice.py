# Dice game code in pyton
import random

def roll_dice():
    return random.randint(1, 6)

def main():
    print("=== Dice Rolling Simulator 🎲 ===")
    while True:
        user_input = input("Press Enter to roll the dice or type 'q' to quit: ").lower()
        
        if user_input == 'q':
            print("Goodbye! 👋")
            break
        
        dice_value = roll_dice()
        print(f"🎲 You rolled a {dice_value}!")

if __name__ == "__main__":
    main()
