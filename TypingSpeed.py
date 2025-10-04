# Typing speed bla bla bla
import time
import random

def typing_speed_test():
    sentences = [
        "Python is a powerful programming language.",
        "I love building projects to improve my skills.",
        "ChatGPT makes learning to code more fun!",
        "Consistency is the key to becoming a great developer."
    ]

    sentence = random.choice(sentences)
    print("=== Typing Speed Test ⌨️ ===")
    print("\nType the following sentence:\n")
    print(sentence)
    input("\nPress Enter when you're ready... ")

    start_time = time.time()
    user_input = input("\nNow type here: ")
    end_time = time.time()

    elapsed_time = end_time - start_time
    words = len(sentence.split())
    speed = words / (elapsed_time / 60)  # words per minute

    print("\n⌛ Time taken: {:.2f} seconds".format(elapsed_time))
    print("⚡ Your typing speed: {:.2f} words per minute (WPM)".format(speed))

    if user_input.strip() == sentence:
        print("✅ Accuracy: 100% (Perfect typing!)")
    else:
        correct_chars = sum(1 for a, b in zip(user_input, sentence) if a == b)
        accuracy = (correct_chars / len(sentence)) * 100
        print(f"🎯 Accuracy: {accuracy:.2f}%")

if __name__ == "__main__":
    typing_speed_test()
