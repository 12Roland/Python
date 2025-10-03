def quiz_game():
    questions = {
        "What is the capital of France?": ["a) Berlin", "b) Paris", "c) Madrid", "d) Rome"],
        "Which programming language is known as the snake language?": ["a) Java", "b) C++", "c) Python", "d) Ruby"],
        "What is 5 + 7?": ["a) 10", "b) 12", "c) 14", "d) 11"],
        "Who developed Facebook?": ["a) Elon Musk", "b) Bill Gates", "c) Mark Zuckerberg", "d) Jeff Bezos"]
    }

    answers = {
        "What is the capital of France?": "b",
        "Which programming language is known as the snake language?": "c",
        "What is 5 + 7?": "b",
        "Who developed Facebook?": "c"
    }

    score = 0
    print("=== Welcome to the Quiz Game 🎮 ===")

    for question, options in questions.items():
        print("\n" + question)
        for option in options:
            print(option)

        answer = input("Enter your answer (a/b/c/d): ").lower()

        if answer == answers[question]:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! The correct answer was {answers[question]}.")

    print(f"\n🏆 Your final score is {score}/{len(questions)}")

if __name__ == "__main__":
    quiz_game()
