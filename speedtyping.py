import random
import time

def generate_random_sentence():
    sentences = [
        "The quick brown fox jumps over the lazy dog.",
        "Python is a powerful and easy-to-read programming language.",
        "The best preparation for tomorrow is doing your best today.",
        "Success is not final, failure is not fatal: It is the courage to continue that counts.",
        "Be yourself; everyone else is already taken.",
        "Happiness is not something readymade. It comes from your own actions.",
        "The only limit to our realization of tomorrow will be our doubts of today."
    ]
    return random.choice(sentences)

def calculate_typing_speed(time_taken, sentence):
    words_per_minute = (len(sentence.split()) / time_taken) * 60
    return words_per_minute

def main():
    print("Welcome to the Speed Typing Test!")
    input("Press Enter to start...")

    sentence = generate_random_sentence()
    print(f"\nType the following sentence as fast as you can:\n{sentence}\n")

    start_time = time.time()

    user_input = input("Start typing: ")

    end_time = time.time()
    time_taken = end_time - start_time

    words_per_minute = calculate_typing_speed(time_taken, sentence)

    correct_words = sum(1 for a, b in zip(user_input.split(), sentence.split()) if a == b)
    accuracy = (correct_words / len(sentence.split())) * 100

    print("\n--- Results ---")
    print(f"Time taken: {time_taken:.2f} seconds")
    print(f"Typing speed: {words_per_minute:.2f} words per minute")
    print(f"Accuracy: {accuracy:.2f}%")

if __name__ == "__main__":
    main()
