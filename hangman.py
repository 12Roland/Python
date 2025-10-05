# Hangman in python pl
import random

def hangman():
    words = ["python", "programming", "developer", "hangman", "university", "software", "engineer"]
    word = random.choice(words)  # pick a random word
    guessed = ["_"] * len(word)  # underscores for unguessed letters
    attempts = 6  # number of wrong guesses allowed
    used_letters = []

    print("=== Welcome to Hangman 🎮 ===")
    print("Guess the word before you run out of attempts!")

    while attempts > 0 and "_" in guessed:
        print("\nWord: ", " ".join(guessed))
        print(f"Attempts left: {attempts}")
        print(f"Used letters: {', '.join(used_letters) if used_letters else 'None'}")

        guess = input("Enter a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("⚠️ Please enter a single alphabet letter.")
            continue

        if guess in used_letters:
            print("You already guessed that letter!")
            continue

        used_letters.append(guess)

        if guess in word:
            print(f"✅ Good guess! '{guess}' is in the word.")
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed[i] = guess
        else:
            print(f"❌ Wrong guess! '{guess}' is not in the word.")
            attempts -= 1

    if "_" not in guessed:
        print(f"\n🎉 Congratulations! You guessed the word: {word}")
    else:
        print(f"\n💀 Game Over! The word was: {word}")

if __name__ == "__main__":
    hangman()
