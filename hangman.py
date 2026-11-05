import random

# Step 1: Define ASCII art stages for Hangman (from 0 to 6 incorrect guesses)
HANGMAN_PICS = [
    """
      +---+
      |   |
          |
          |
          |
          |
    =========""",
    """
      +---+
      |   |
      O   |
          |
          |
          |
    =========""",
    """
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========""",
    """
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========""",
    """
      +---+
      |   |
      O   |
     /|\\  |
          |
          |
    =========""",
    """
      +---+
      |   |
      O   |
     /|\\  |
     /    |
          |
    =========""",
    """
      +---+
      |   |
      O   |
     /|\\  |
     / \\  |
          |
    =========""",
]


def play_hangman():
    """Executes a single round of the Hangman console game."""
    
    # Step 2: Initialize the word bank and select a random target word
    words = ["python", "coding", "matrix", "planet", "guitar"]
    secret_word = random.choice(words)

    # Step 3: Set up game state tracking variables
    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect = len(HANGMAN_PICS) - 1  # Dynamically set to 6

    print("\n=========================================")
    print("           WELCOME TO HANGMAN!           ")
    print("=========================================")
    print(f"Word Bank: {', '.join(words)}")
    print(f"The secret word has {len(secret_word)} letters.")
    print(f"You have {max_incorrect} incorrect guesses allowed.\n")

    # Step 4: Execute the main game loop until the player wins or runs out of guesses
    while incorrect_guesses < max_incorrect:
        # Render current gallows graphic
        print(HANGMAN_PICS[incorrect_guesses])

        # Construct the masked word string (e.g., "p _ t h _ n")
        display_word = " ".join(
            [letter if letter in guessed_letters else "_" for letter in secret_word]
        )

        print(f"\nWord: {display_word}")
        print(f"Incorrect guesses remaining: {max_incorrect - incorrect_guesses}")
        print(
            f"Guessed letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}"
        )

        # Step 5: Check win condition (no underscores remaining)
        if "_" not in display_word:
            print("\n=========================================")
            print(f"CONGRATULATIONS! You guessed the word: '{secret_word.upper()}'!")
            print("=========================================")
            break

        # Step 6: Prompt player for input and sanitize it
        guess = input("\nEnter a single letter: ").lower().strip()

        # Step 7: Validate player input for format and repetition
        if len(guess) != 1 or not guess.isalpha():
            print("[!] Invalid input. Please enter a single alphabetical character.")
            continue

        if guess in guessed_letters:
            print(f"[!] You have already guessed '{guess}'. Please try a different letter.")
            continue

        # Record the validated guess
        guessed_letters.append(guess)

        # Step 8: Evaluate the guessed letter against the secret word
        if guess in secret_word:
            print(f"[+] Good job! '{guess}' is in the word.")
        else:
            incorrect_guesses += 1
            print(f"[-] Sorry, '{guess}' is not in the word.")

    # Step 9: Handle loss condition if maximum incorrect guesses are reached
    if incorrect_guesses == max_incorrect:
        print(HANGMAN_PICS[incorrect_guesses])
        print("\n=========================================")
        print("               GAME OVER!                ")
        print(f"You ran out of guesses. The word was: '{secret_word.upper()}'.")
        print("=========================================")


def main():
    """Manages the overall application flow and replay loop."""
    # Step 10: Run the game loop and offer a replay option upon completion
    while True:
        play_hangman()
        replay = input("\nWould you like to play again? (y/n): ").lower().strip()
        if replay not in ("y", "yes"):
            print("\nThank you for playing Hangman! Goodbye.")
            break


if __name__ == "__main__":
    main()