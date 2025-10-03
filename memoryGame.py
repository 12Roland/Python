import random
import time

def memory_game():
    print("=== Memory Game 🧠 ===")
    print("Match the pairs by remembering their positions!")

    # Create pairs of numbers
    numbers = list(range(1, 5)) * 2  # 4 pairs = 8 cards
    random.shuffle(numbers)

    board = ["*"] * 8
    revealed = [False] * 8

    while not all(revealed):
        print("\nBoard:", " ".join(board))

        try:
            choice1 = int(input("Pick the first position (0-7): "))
            choice2 = int(input("Pick the second position (0-7): "))
        except ValueError:
            print("⚠️ Enter valid numbers between 0 and 7.")
            continue

        if choice1 == choice2 or choice1 not in range(8) or choice2 not in range(8):
            print("Invalid choices. Try again.")
            continue

        # Reveal choices
        board[choice1] = str(numbers[choice1])
        board[choice2] = str(numbers[choice2])
        print("\nBoard:", " ".join(board))
        time.sleep(1)

        if numbers[choice1] == numbers[choice2]:
            print("✅ Match found!")
            revealed[choice1] = True
            revealed[choice2] = True
        else:
            print("❌ No match!")
            board[choice1] = "*"
            board[choice2] = "*"

    print("\n🎉 Congratulations! You matched all pairs.")

if __name__ == "__main__":
    memory_game()
