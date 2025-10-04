# Flashcard app in python
import json

# Load flashcards from a file (if exists)
def load_flashcards():
    try:
        with open("flashcards.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

# Save flashcards to a file
def save_flashcards(cards):
    with open("flashcards.json", "w") as f:
        json.dump(cards, f, indent=4)

# Add a new flashcard
def add_flashcard(cards):
    question = input("Enter the question: ")
    answer = input("Enter the answer: ")
    cards[question] = answer
    save_flashcards(cards)
    print("✅ Flashcard added!")

# Review flashcards
def review_flashcards(cards):
    if not cards:
        print("⚠️ No flashcards available. Add some first!")
        return
    for question, answer in cards.items():
        print(f"\n❓ {question}")
        input("Press Enter to see the answer...")
        print(f"💡 Answer: {answer}")

# Main menu
def main():
    flashcards = load_flashcards()
    while True:
        print("\n--- Flashcard App ---")
        print("1. Add flashcard")
        print("2. Review flashcards")
        print("3. Exit")

        choice = input("Choose an option: ")
        if choice == "1":
            add_flashcard(flashcards)
        elif choice == "2":
            review_flashcards(flashcards)
        elif choice == "3":
            print("👋 Goodbye!")
            break
        else:
            print("Invalid choice. Try again!")

if __name__ == "__main__":
    main()
