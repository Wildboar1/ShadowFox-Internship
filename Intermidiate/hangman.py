import random

def play_hangman():
    #Word Selection
    words = ['python', 'developer', 'algorithm', 'function', 'variable', 'syntax']
    word = random.choice(words).upper()
    
    #Game Setup
    guessed_letters = []
    incorrect_guesses = 0
    max_attempts = 6
    
    print("--- Welcome to Hangman! ---")

    #Game Loop
    while incorrect_guesses < max_attempts:
        #Display Interface
        print_hangman(incorrect_guesses)
        
        display_word = ""
        for letter in word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "
        
        print(f"\nWord: {display_word}")
        print(f"Guessed letters: {', '.join(guessed_letters)}")
        print(f"Attempts remaining: {max_attempts - incorrect_guesses}")

        #Win Condition
        if "_" not in display_word:
            print("\nCongratulations! You won!")
            break

        #User Input & Validation
        guess = input("Guess a letter: ").upper()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try again.")
            continue

        guessed_letters.append(guess)

        #Check Guess
        if guess in word:
            print(f"Good job! '{guess}' is in the word.")
        else:
            print(f"Sorry, '{guess}' is not there.")
            incorrect_guesses += 1

    #LossCondition
    if incorrect_guesses == max_attempts:
        print_hangman(incorrect_guesses)
        print(f"\nGame Over! The word was: {word}")

    #Play Again
    restart = input("\nWould you like to play again? (y/n): ").lower()
    if restart == 'y':
        play_hangman()
    else:
        print("Thanks for playing!")

def print_hangman(errors):
    """Simple text-based interface for the hangman figure."""
    stages = [
        "  +---+\n  |   |\n      |\n      |\n      |\n      |\n=========",
        "  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n=========",
        "  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========",
        "  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n=========",
        "  +---+\n  |   |\n  O   |\n /|\\  |\n      |\n      |\n=========",
        "  +---+\n  |   |\n  O   |\n /|\\  |\n /    |\n      |\n=========",
        "  +---+\n  |   |\n  O   |\n /|\\  |\n / \\  |\n      |\n========="
    ]
    print(stages[errors])

if __name__ == "__main__":
    play_hangman()