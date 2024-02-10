import random

# Import the word list and the game logo from external files
from hangman_words import word_list
from hangman_art import logo, stages

# Select a random word from the word list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

# Print the game logo at the start
print(logo)

# Create a list of underscores to represent the hidden word
display = ["_" for _ in range(word_length)]

# Main game loop
while not end_of_game:
    # Get a letter input from the player
    guess = input("Guess a letter: ").lower()

    # Check if the letter has already been guessed
    if guess in display:
        print(f"You've already guessed {guess}")

    # Check if the guessed letter is in the chosen word
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    # If the guessed letter is not in the chosen word, reduce lives and print feedback
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1

        # End the game if no lives left
        if lives == 0:
            end_of_game = True
            print("You lose.")

    # Display the current state of the word
    print(f"{' '.join(display)}")

    # Check if the player has guessed all letters in the word
    if "_" not in display:
        end_of_game = True
        print("You win.")

    # Display the current stage of the hangman based on remaining lives
    print(stages[lives])
